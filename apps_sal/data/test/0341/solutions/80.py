(n, k) = map(int, input().split())
(r, s, p) = map(int, input().split())
t = list(input())
rsp = {'r': p, 's': r, 'p': s}
sumt = 0
chk = [1] * n
for i in range(len(t)):
    sumt += rsp[t[i]]
    if i >= k and t[i] == t[i - k]:
        chk[i] = chk[i - k] + 1
        chk[i - k] = 1
ans = sumt
for i in range(len(chk)):
    if chk[i] != 1:
        chg = chk[i] // 2
        ans -= rsp[t[i]] * chg
print(ans)
