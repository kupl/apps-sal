def f(x):
    tmp = x
    z = 0
    while tmp % 2 == 0:
        tmp //= 2
        z += 1
    return [tmp, z]

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sl = dict()
    for x in a:
        y, z = f(x)
        if sl.get(y) == None:
            sl[y] = z
        else:
            sl[y] = max(sl[y], z)
    ans = 0
    for x in sl.keys():
        ans += sl[x]
    print(ans)
