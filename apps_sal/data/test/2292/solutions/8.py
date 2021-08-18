import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = []
    D = []

    if n % 2 == 1:
        if A[n // 2] != B[n // 2]:
            print("No")
            continue

    for i in range(n // 2):
        C.append(sorted([A[i], A[-i - 1]]))
        D.append(sorted([B[i], B[-i - 1]]))

    if sorted(C) == sorted(D):
        print("Yes")
    else:
        print("No")
