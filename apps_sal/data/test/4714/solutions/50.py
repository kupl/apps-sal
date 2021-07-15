a,b = list(map(int, input().split()))

ans = 0
for i in range(a, b+1):
    s = str(i)
    ok = True
    for j in range(2):
        ok = ok and s[j] == s[4-j]
    if ok:
        ans += 1

print(ans)

