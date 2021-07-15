def main():

    n, x, y = map(int,input().split())

    cnt = 0

    ans=[0]*n

    for i in range(1,n+1):
        for j in range(i+1,n+1):
            d = min(j-i,abs(x-i)+abs(y-j)+1)
            ans[d] += 1

    for i in range(1,n):
        print(ans[i])
   
def __starting_point():
    main()
__starting_point()
