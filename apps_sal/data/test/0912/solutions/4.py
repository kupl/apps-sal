for i in range(int(input())):
    (n, s, k) = [int(i) for i in input().split()]
    l = set([int(i) for i in input().split()])
    i = 0
    res = 0
    while 1:
        if s + i <= n and s + i not in l:
            break
        if s - i >= 1 and s - i not in l:
            break
        i += 1
        res += 1
    print(res)
