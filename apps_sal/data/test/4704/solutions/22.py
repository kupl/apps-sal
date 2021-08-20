import itertools
n = int(input())
a = [0] + list(map(int, input().split()))
a = list(itertools.accumulate(a))
ans = 1000000000000000.0
for i in range(1, n):
    ans = min(ans, abs(a[n] - 2 * a[i]))
print(ans)
