def main():
    import sys
    input = lambda:sys.stdin.readline().strip()
    
    N = int(input())
    A = list(map(int,input().split()))

    #i%2==0を加算、i%2==1を減算すれば山1の高さになる。
    tmp = 0
    for i in range(N):
        if i%2==0:
            tmp+=A[i]
        else:
            tmp-=A[i]

    ans = [tmp]
    for i in range(N-1):
        tmp = (A[i]-tmp//2)*2
        ans.append(tmp)

    print(*ans)
        
def __starting_point():
    main()
__starting_point()
