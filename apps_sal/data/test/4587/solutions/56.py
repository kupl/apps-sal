import bisect

n = int(input())
al = sorted(list(map(int, input().split())))
bl = sorted(list(map(int, input().split())))
cl = sorted(list(map(int, input().split())))
ans = 0

for b in bl:
    i = bisect.bisect_left(al, b)
    j = bisect.bisect_right(cl, b)
    ans += i*(n-j)

print(ans)
