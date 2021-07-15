from bisect import bisect_right

n, m, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt = 0
a_cum = [0] * (n + 1)
b_cum = [0] * (m + 1)

for i in range(n):
    a_cum[i+1] = a_cum[i] + a[i]
for i in range(m):
    b_cum[i+1] = b_cum[i] + b[i]

for i in range(n+1):
    a_cnt = i
    rest = k - a_cum[i]
    if rest < 0:
        break
    b_cnt = bisect_right(b_cum,rest) - 1    
    cnt = max(cnt, a_cnt + b_cnt)

print(cnt)
