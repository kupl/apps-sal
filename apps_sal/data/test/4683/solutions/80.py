import itertools

n = int(input())
a = list(map(int, input().split()))
ans = 0

lis = list(itertools.accumulate(reversed(a)))

for i in range(n - 1):
    ans += a[i] * lis[n - 2 - i]

print(ans % (10**9 + 7))
