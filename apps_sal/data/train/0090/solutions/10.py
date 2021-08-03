import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    l = list(map(int, input().split()))

    B = []
    for i in range(n):
        if l[i] == 0:
            B.append(A[i])
    B.sort(reverse=True)

    ind = 0
    for i in range(n):
        if l[i] == 0:
            A[i] = B[ind]
            ind += 1

    print(*A)
