for _ in range(int(input())):
    n = int(input())
    l = [input().strip() for i in range(n)]
    prob = 0
    odd = 0
    for i in range(n):
        z = l[i].count('0')
        o = l[i].count('1')
        if len(l[i]) % 2 == 1:
            odd = 1
            break
        elif z % 2 == 1:
            prob += 1
    if odd == 1:
        print(n)
    elif prob % 2 == 1:
        print(n - 1)
    else:
        print(n)
