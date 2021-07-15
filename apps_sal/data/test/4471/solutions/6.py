def one():
    return int(input())


def more():
    return list(map(int, input().split()))


for _ in range(one()):
    n = one()
    l = list(more())
    s = 0
    for i in l:
        s += i % 2
    if s%n==0:
        print('YES')
    else:
        print('NO')

