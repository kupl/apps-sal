import sys
input = sys.stdin.readline

q=int(input())

for testcases in range(q):
    n,r=list(map(int,input().split()))
    E=list(map(int,input().split()))

    E.append(0)

    E=sorted(set(E))

    for i in range(1,n+1):
        if E[-i-1]<=r*i:
            print(i)
            break
        

    

    

