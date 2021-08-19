N = int(input())
A = list(map(int, input().split()))
B = [0 for i in range(N)]
B[0] = 2
while 1:
    for i in range(1, N):
        B[i] = 2 * A[i] - B[i - 1]
    if B[0] == 2 * A[0] - B[-1]:
        break
    else:
        B[0] = (B[0] + (2 * A[0] - B[-1])) // 2
B = [B[-1]] + B[:-1]
print(*B)
