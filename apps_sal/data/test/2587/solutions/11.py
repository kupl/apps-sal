for t in range(int(input())):
    n=int(input())
    ans='9'*n
    k=(n+3)//4
    print(ans[:-k]+k*'8')
