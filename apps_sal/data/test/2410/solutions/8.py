import sys
input = sys.stdin.readline

from itertools import accumulate

t=int(input())

for test in range(t):
    n=int(input())
    A=list(map(int,input().split()))

    S=list(accumulate(A))

    for s in S:
        if s<=0:
            print("NO")
            break

    else:
        B=A[::-1]

        S=list(accumulate(B))

        for s in S:
            if s<=0:
                print("NO")
                break

        else:
            print("YES")
        


