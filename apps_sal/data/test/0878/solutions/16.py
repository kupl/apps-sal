def solve(n,A):
    cnt=0
    for i in range(n-1):
        a0,a1,a2=A[i],A[i+1],A[i+2]
        if a2==1:
            if a1==2:
                cnt+=3
            else:
                cnt+=4
        elif a2==2:
            if a1==1:
                if a0==3:
                    cnt+=2
                else:
                    cnt+=3
            else:
                print('Infinite')
                return
        else:
            if a1==1:
                cnt+=4
            else:
                print('Infinite')
                return
    print('Finite')
    print(cnt)
    return

n=int(input())
A=[0]+list(map(int,input().split()))
solve(n,A)
