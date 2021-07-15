def main():
    a,b = list(map(int,input().split()))
    def f(n):
        if n%4==0:
            return n
        if n%4==1:
            return 1
        if n%4==2:
            return n + 1
        if n%4==3:
            return 0
    print((f(b)^f(a-1)))

def __starting_point():
    main()

__starting_point()
