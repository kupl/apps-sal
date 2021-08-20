N = int(input())
D = list(map(int, input().split()))
Sum = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        A = D[i] * D[j]
        Sum += A
print(Sum)
