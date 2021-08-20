N = int(input())
A = list(map(int, input().split()))
print(max(A) ^ A[N - 1])
