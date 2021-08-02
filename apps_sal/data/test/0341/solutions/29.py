n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

rsp = {"r": p, "s": r, "p": s}
ans = 0
for i in range(n):
    if i < k:
        ans += rsp[t[i]]
    else:
        if t[i] != t[i - k]:
            ans += rsp[t[i]]
        else:
            t[i] = "a"
print(ans)
