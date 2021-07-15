from itertools import accumulate
N = int(input())
A = tuple(accumulate(map(int, input().split())))
x = A[-1]
y = A[0]
ans = abs(x - y - y)
for a in A[:-1]:
    ans = min(ans, abs(x - a - a))
print(ans)
