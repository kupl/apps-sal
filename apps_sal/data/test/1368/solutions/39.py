from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N,A,B=map(int,readline().split())
    v=list(map(int,readline().split()))
    v.sort(reverse=True)

    #average
    average=sum(v[:A])/A

    #combination
    res=0
    x=v[A-1]
    x_count=v.count(x)
    x_count_copy=x_count
    if x==v[0]:
        up=1
        down=1
        for i in range(1,A):
            up*=x_count_copy
            x_count_copy-=1
            down*=i
        if x_count>=B:
            for i in range(A,B+1):
                up*=x_count_copy
                x_count_copy-=1
                down*=i
                res+=up//down
        else:
            for i in range(A,x_count+1):
                up*=x_count_copy
                x_count_copy-=1
                down*=i
                res+=up//down
    else:
        m=A
        for i in range(A):
            if v[i]>x:
                m-=1
            else:
                break
        up=1
        down=1
        for i in range(1,m+1):
            up*=x_count_copy
            x_count_copy-=1
            down*=i
        res=up//down

    print(average)
    print(res)
    
def __starting_point():
    main()
__starting_point()
