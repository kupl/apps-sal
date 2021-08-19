import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
ans = 0
for i in b:
    p = bisect.bisect_left(a, i)
    q = bisect.bisect_right(c, i)
    ans += p * (n - q)
print(ans)
