import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    n,k=list(map(int,input().split()))

    if n%2==k%2 and n>=k:
        print("YES")
        ANS=[1]*(k-1)+[n-(k-1)]
        print(*ANS)

    elif n%2==0 and n>=2*k:
        print("YES")
        ANS=[2]*(k-1)+[n-2*(k-1)]
        print(*ANS)
    else:
        print("NO")
        
        
        

