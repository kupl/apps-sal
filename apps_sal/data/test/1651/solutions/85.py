def resolve():
    # n=int(input())
    # a,b=map(int,input().split())
    # x=list(map(int,input().split()))
    #a=[list(map(lambda x:int(x)%2,input().split())) for _ in range(h)]
    s, p = map(int, input().split())
    ans = 'No'
    for n in range(1, int(p**(1 / 2)) + 1):
        if p % n == 0:
            if (p // n) + n == s:
                ans = 'Yes'
                break
    print(ans)


def __starting_point():
    resolve()


__starting_point()
