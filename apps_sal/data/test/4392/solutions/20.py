import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    (n, m) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    P = set(map(int, input().split()))
    flag = 1
    for i in range(n):
        top = i
        for j in range(n - 1, i, -1):
            if A[i] > A[j]:
                top = j + 1
                break
        for j in range(i + 1, top):
            if j in P:
                continue
            else:
                flag = 0
                break
        if flag == 0:
            break
    if flag:
        print('YES')
    else:
        print('NO')
