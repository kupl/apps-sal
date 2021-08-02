N = int(input())
for i in range(N):
    A = int(input())
    B = list(map(int, input().split()))
    B.sort()
    flag = True
    for i in range(2 * A):
        if B[2 * i] != B[2 * i + 1]:
            flag = False
            break
    S = B[0] * B[-1]
    for i in range(A):
        if B[i * 2] * B[-i * 2 - 1] != S:
            flag = False
            break
    print(["NO", "YES"][flag])
