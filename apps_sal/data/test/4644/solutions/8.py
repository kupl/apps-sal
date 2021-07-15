t = int(input())
for zz in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ha = False
    ho = False
    he = False
    for i in a:
        if i % 2 == 1:
            ho = True
        else:
            he = True
    if n % 2 == 0:
        ha = ho and he
    else:
        ha = ho
    if ha:
        print('YES')
    else:
        print('NO')

