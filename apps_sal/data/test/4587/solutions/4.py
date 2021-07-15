import bisect

n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
ans = 0

for b in B:
    a = bisect.bisect_left(A, b)
    c = bisect.bisect_right(C, b)
    ans += a*(n-c)

print(ans)
