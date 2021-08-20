import bisect
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
ans = i = j = 0
for b in B:
    i = bisect.bisect_left(A, b)
    j = N - bisect.bisect_right(C, b)
    ans += i * j
print(ans)
