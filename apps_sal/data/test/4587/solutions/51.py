import bisect
n = int(input())
(a, b, c) = map(list, [sorted(list(map(int, input().split()))) for i in range(3)])
ans = 0
for i in range(n):
    ans += bisect.bisect_left(a, b[i]) * (n - bisect.bisect_right(c, b[i]))
print(ans)
