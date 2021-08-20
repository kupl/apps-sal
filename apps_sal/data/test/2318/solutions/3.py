import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    A = input().strip()
    B = input().strip()
    AA = []
    AA.append([A[0], 1])
    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            AA[-1][1] += 1
        else:
            AA.append([A[i], 1])
    BB = []
    BB.append([B[0], 1])
    for i in range(1, len(B)):
        if B[i] == B[i - 1]:
            BB[-1][1] += 1
        else:
            BB.append([B[i], 1])
    if len(AA) != len(BB):
        print('NO')
    else:
        for i in range(len(AA)):
            if AA[i][0] == BB[i][0] and AA[i][1] <= BB[i][1]:
                continue
            else:
                print('NO')
                break
        else:
            print('YES')
