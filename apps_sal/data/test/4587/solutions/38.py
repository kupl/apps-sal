from bisect import bisect, bisect_left

N = int(input())
A, B, C = (sorted(map(int, input().split())) for _ in range(3))

ans = 0
for b in B:
  ans += bisect_left(A, b) * (N - bisect(C, b))

print(ans)
