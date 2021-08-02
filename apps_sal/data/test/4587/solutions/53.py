import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a = sorted(a)
c = sorted(c)
ans = 0
for i in b:
    t = bisect.bisect_left(a, i)
    q = bisect.bisect_right(c, i)
    ans += t * (n - q)
print(ans)
