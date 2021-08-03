t = int(input())


def power(n):
    res = 0
    while n % 2 == 0:
        res += 1
        n //= 2
    if n not in d:
        d[n] = 0
    d[n] = max(d[n], res)


for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxx = 0
    d = {}
    for num in a:
        power(num)
    print(sum(list(d.values())))
    # print(maxx)
