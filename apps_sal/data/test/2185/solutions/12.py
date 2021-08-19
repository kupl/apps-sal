import sys
input = sys.stdin.readline
t = int(input())
for testcases in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [B[i] - A[i] for i in range(n)]
    MAX = max(C)
    if min(C) < 0:
        print('NO')
        continue
    if MAX == 0:
        print('YES')
        continue
    for c in C:
        if 0 < c < MAX:
            print('NO')
            break
    else:
        D = []
        for i in range(n):
            if C[i] == MAX:
                D.append(i)
        if len(D) <= 1:
            print('YES')
            continue
        for j in range(1, len(D)):
            if D[j] != D[j - 1] + 1:
                print('NO')
                break
        else:
            print('YES')
