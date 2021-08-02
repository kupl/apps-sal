m, n = list(map(int, input().split()))
s = [set([int(x) for x in input().split()][1:]) for _ in range(m)]
ok = True
for i in range(m):
    for j in range(i + 1, m):
        if not s[i] & s[j]:
            ok = False
            break
    if not ok:
        break
print(("" if ok else "im") + "possible")
