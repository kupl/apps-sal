n, m = list(map(int, input().split()))
for g in range(m):
    l = list(map(int, input().split()))
    s = set(l[1:])
    found = False
    for e in l[1:]:
        f = -e
        if f in s:
            found = True
            break
    if not found:
        print("YES")
        return
print("NO")

