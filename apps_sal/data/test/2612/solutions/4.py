import sys
def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    n = int(input())
    S = [int(i) for i in input().split()]
    A = [1] * (n + 1)
    for i in range(1, n + 1):
        mul = 2
        while i * mul <= n:
            if S[i * mul - 1] > S[i - 1]:
                A[i * mul] = max(A[i * mul], A[i] + 1)
            mul += 1
    print(max(A))
