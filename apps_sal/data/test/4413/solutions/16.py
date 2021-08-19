for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    l.sort()
    res = 1
    for i in range(n - 1):
        if l[i] + 1 == l[i + 1]:
            res = 2
            break
    print(res)
