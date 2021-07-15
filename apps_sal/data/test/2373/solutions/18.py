# 前から順番に後ろに向けてswap
n = int(input())
ps = list(map(int, input().split()))

cnt = 0
for i in range(n-1):
    if i + 1 == ps[i]:
        tmp = ps[i]
        ps[i] = ps[i+1]
        ps[i+1] = tmp
        cnt += 1
# 最後残っていたら直前とswap
if ps[n-1] == n:
    cnt += 1

print(cnt)

