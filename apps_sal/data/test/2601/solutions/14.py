t = int(input())
for you in range(t):
    n = int(input())
    l = input().split()
    li = [int(i) for i in l]
    poss = 1
    for i in range(n - 1):
        if li[i] > li[i + 1]:
            continue
        poss = 0
        break
    if poss:
        print('NO')
    else:
        print('YES')
