
def main():
    pass


def __starting_point():
    main()


k, a, b, v = list(map(int, input().split()))
n = 0
if(b < k):
    a -= ((b + 1) * v)
    n += 1
    while(a > 0):
        a -= v
        n += 1
    print(n)
else:
    while((b >= k) and (a > 0)):
        b -= (k - 1)
        a -= (k * v)
        n += 1
    if(a > 0):
        a -= ((b + 1) * v)
        n += 1
        while(a > 0):
            a -= v
            n += 1
    print(n)

__starting_point()
