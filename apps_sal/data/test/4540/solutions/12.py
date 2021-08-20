N = int(input())
A = list(map(int, input().split()))
B = A[:]
B.insert(0, 0)
B.append(0)
sum = 0
for i in range(N + 1):
    sum += abs(B[i + 1] - B[i])
for i in range(N):
    x = abs(B[i + 1] - B[i]) + abs(B[i + 2] - B[i + 1])
    y = abs(B[i + 2] - B[i])
    print(sum - x + y)
