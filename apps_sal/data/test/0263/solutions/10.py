n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]

ans = [max(a), max(a) + m]
d = m - n * max(a) + sum(a)
if 0 < d:
    ans[0] += (d + n - 1) // n

print(" ".join(map(str, ans)))

