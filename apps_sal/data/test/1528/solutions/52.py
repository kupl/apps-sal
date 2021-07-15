
        
def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    def f(n, x):
        if n == 0:
            return 0 if x<=0 else 1
        elif x <= a[n-1]+1:
            return f(n-1, x-1)
        else:
            return p[n-1]+1+f(n-1, x-2-a[n-1])

    n, x = map(int, input().split())
    a, p = [1], [1]
    for i in range(n):
        a.append(2*a[-1]+3)
        p.append(2*p[-1]+1)
    print(f(n, x))





                
def __starting_point():
    main()
__starting_point()
