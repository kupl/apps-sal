import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    if sum(A) == 0:
        print('NO')
    elif sum(A) > 0:
        B = []
        C = []
        Z = []
        for a in A:
            if a > 0:
                B.append(a)
            elif a < 0:
                C.append(a)
            else:
                Z.append(a)
        print('YES')
        print(*B + Z + C)
    else:
        B = []
        C = []
        Z = []
        for a in A:
            if a > 0:
                B.append(a)
            elif a < 0:
                C.append(a)
            else:
                Z.append(a)
        print('YES')
        print(*C + Z + B)
