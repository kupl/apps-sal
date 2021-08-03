def resolve():
    # n=int(input())
    # a,b=map(int,input().split())
    # x=list(map(int,input().split()))
    #a=[list(map(lambda x:int(x)%2,input().split())) for _ in range(h)]
    a, b, x, y = map(int, input().split())
    if b >= a:
        print((b - a) * min(2 * x, y) + x)
    else:
        print((a - b - 1) * min(2 * x, y) + x)


def __starting_point():
    resolve()


__starting_point()
