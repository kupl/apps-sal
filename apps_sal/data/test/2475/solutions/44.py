import itertools
N = int(input())
S = [int(_) for _ in input().split()]
ans = 0
for i in range(1, N - 1):
    maxj = (N - 1) // i
    if (N - 1) % i == 0:
        maxj = ((N - 1) // i + 1) // 2
    dp = itertools.accumulate((x + y for (x, y) in zip(S[:i * maxj:i], S[-1:-1 - i * maxj:-i])))
    ans = max(ans, max(dp))
print(ans)
