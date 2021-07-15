import sys
input = sys.stdin.readline
t = int(input())
for ii in range(t):
    n, x = map(int,input().split())
    A = list(map(int,input().split()))
    B = []
    c = A.count(x)
    for i in range(n):
        if A[i] != x:
            B.append(A[i])

    if B == []:
        print(0)
    elif c > 0 or sum(B) == x*len(B):
        print(1)
    else:
        print(2)
