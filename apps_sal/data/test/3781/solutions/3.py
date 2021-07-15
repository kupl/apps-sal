T=int(input())
for testcase in range(T):
    N=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    if N%2==0:
        flag=1
        for i in range(N//2):
            if a[2*i]!=a[2*i+1]:
                flag=0
                break
        if flag:
            print("Second")
        else:
            print("First")
    else:
        print("Second")
        

