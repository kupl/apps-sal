import sys


def r():
    return list(map(int, input().split()))


n, k = list(map(int, input().split()))
a = r()

sum = 0
cnt = 0
for i in range(n):
    sum += a[i]
    cnt += min(8, sum)
    sum = max(0, sum - 8)
    if (cnt >= k):
        print(i + 1)
        return

print(-1)
