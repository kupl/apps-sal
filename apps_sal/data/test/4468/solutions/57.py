N, T = map(int, input().split())
t = list(map(int, input().split()))
t.append(10**10)
ans = 0
flg = 0
temp = 0

for i in range(N):
    if t[i] + T > t[i + 1]:
        if flg == 0:
            temp = t[i]
            flg = 1
        continue
    else:
        if flg == 0:
            ans += T
        else:
            ans += t[i] - temp + T
        flg = 0
print(ans)
