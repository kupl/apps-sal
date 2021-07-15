import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
c.sort()

ans = 0
for B in b:
    i = bisect.bisect_left(a, B)
    j = bisect.bisect_right(c, B)
    ans += i * (n - j)

print(ans)
