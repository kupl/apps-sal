from itertools import accumulate
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
a = list([int(x) - 1 for x in input().split()])

cnt0 = [0] * m
cnt1 = [0] * m
for i in range(n-1):
    cnt0[a[i+1]] += (a[i+1] - a[i]) % m - 1
    if (a[i] + 1) % m <= a[i+1]:
        cnt1[(a[i]+1) % m] += 1
        cnt1[a[i+1]] -= 1
    else:
        cnt1[(a[i]+1) % m] += 1
        cnt1[0] += 1
        cnt1[a[i+1]] -= 1
cnt1 = list(accumulate(cnt1))
ans = float('inf')
tmp = 0
for i in range(n-1):
    tmp += min((a[i+1] - a[i]) % m, a[i+1] + 1)
ans = tmp
for i in range(m-1):
    tmp += cnt0[i] - cnt1[i]
    ans = min(ans, tmp)
print(ans)


