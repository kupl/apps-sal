def product_max(a,b,c,d):
    print(max(a*c, a*d, b*c, b*d))

def __starting_point():
    a,b,c,d = map(int, input().split())
    product_max(a,b,c,d)
__starting_point()
