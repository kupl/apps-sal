import sys
input = sys.stdin.readline


def query(n, A):
    A.sort()
    B = []
    for i in range(0, n * 4, 2):
        if A[i] != A[i + 1]:
            return 'NO'
        B.append(A[i])
    s = B[0] * B[-1]
    for i in range(n * 2):
        if B[i] * B[-i - 1] != s:
            return 'NO'
    return 'YES'


q = int(input())
for _ in range(q):
    n = int(input())
    A = list(map(int, input().split()))
    print(query(n, A))
