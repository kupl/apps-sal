for i in range(int(input())):
    n = int(input())
    l = []
    a = 4 * n
    for j in range(n):
        l.append(a)
        a -= 2
    print(*l)
