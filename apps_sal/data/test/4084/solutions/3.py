def main():
    n,a,b = map(int, input().split())
    f = a * (n//(a+b))
    l = n%(a+b)
    rest  = 0
    if l < a:
        rest = l
    else:
        rest = a
    return f+rest
    
def __starting_point():
    print(main())
__starting_point()
