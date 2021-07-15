import math

n, k = map(int, input().split())
ans = []
i = k + 1
if i > n:
    print(1)
    print(math.ceil(n / 2))
    return
while i <= n:
    ans.append(i)
    i += 2 * k + 1
if ans[-1] + k < n:
    ned = 2 * k - (n - ans[-1]) + 1
    print(len(ans) + 1)
    for i in ans:
        print(i - ned, end = " ")
    print(n)
else:
    print(len(ans))
    print(*ans)

