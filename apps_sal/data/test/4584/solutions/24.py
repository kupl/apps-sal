N = int(input())
A = [int(i) for i in input().split()]
ans = [0] * N
for i in range(N - 1):
    ans[A[i] - 1] += 1
for i in ans:
    print(i)
