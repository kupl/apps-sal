N = int(input()) + 2
A = [0]
A.extend(list(map(int, input().split())))
A.append(0)
B = sum((abs(A[i] - A[i - 1]) for i in range(1, N)))
for i in range(1, N - 1):
    print(B - abs(A[i] - A[i - 1]) - abs(A[i + 1] - A[i]) + abs(A[i + 1] - A[i - 1]))
