import math
n = int(input())
A = list(map(int, input().split()))


def combinations_count(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


ans = dict()
for a in A:
    if a in ans:
        ans[a] += 1
    else:
        ans[a] = 1
prin = 0
for a in ans:
    prin += combinations_count(ans[a], 2)
for i in range(n):
    print(prin - ans[A[i]] + 1)
