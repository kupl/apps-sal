import bisect
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    aa = bisect.bisect_left(a, b[i])
    ca = n - bisect.bisect_right(c, b[i])
    ans += aa * ca
print(ans)
