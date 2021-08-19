N = int(input())
A = list(map(int, input().split()))
Q = int(input())
nums = [0] * 100000
for i in range(N):
    nums[A[i] - 1] += 1
S = 0
for j in range(100000):
    S += (j + 1) * nums[j]
for j in range(Q):
    (B, C) = map(int, input().split())
    S += nums[B - 1] * (C - B)
    nums[C - 1] += nums[B - 1]
    nums[B - 1] = 0
    print(S)
