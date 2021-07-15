N = int(input())
A = list(map(int,input().split()))

# 0
# 1, 0
# 2, 0, 1
# 3, 1, 0, 2
# 4, 2 ,0, 1, 3

ans = None
if N % 2 == 1:
  ans = A[::2][::-1] + A[1::2]
else:
  ans = A[1::2][::-1] + A[::2]
print(*ans)
