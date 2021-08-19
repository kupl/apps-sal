N = int(input())
A = list(map(int, input().split()))
total = abs(A[0]) + abs(A[-1])
for i in range(N - 1):
    total += abs(A[i] - A[i + 1])
ans = total - abs(A[0]) - abs(A[0] - A[1]) + abs(A[1])
print(ans)
for i in range(N - 2):
    ans = total - abs(A[i] - A[i + 1]) - abs(A[i + 1] - A[i + 2]) + abs(A[i] - A[i + 2])
    print(ans)
ans = total - abs(A[-1]) - abs(A[-1] - A[-2]) + abs(A[-2])
print(ans)
