import sys
n, m = list(map(int, input().split()))


def xor(A):
    x = 0
    for a in A:
        x ^= a
    return x


A = [[int(x) for x in input().split()] for _ in range(n)]

I = [0] * n

ref = A[0][0]
if xor(A[i][0] for i in range(n)):
    print('TAK')
    print(*[i + 1 for i in I])
    return
else:
    for i in range(n):
        for j in range(m):
            if A[i][0] != A[i][j]:
                I[i] = j
                print('TAK')
                print(*[i + 1 for i in I])
                return
print('NIE')
