import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
ans = 0
for i in b:
    an = bisect.bisect_left(a, i)
    cn = n - bisect.bisect_right(c, i)
    ans += an * cn

print(ans)

