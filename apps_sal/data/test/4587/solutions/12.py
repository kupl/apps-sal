from bisect import bisect, bisect_left
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
ans = 0
for b in B:
    i = bisect_left(A, b)
    j = bisect(C, b)
    ans += i * (N - j)
print(ans)
