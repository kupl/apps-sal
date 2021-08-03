for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    ans = [["0" for j in range(n)] for i in range(n)]
    posx = 0
    posy = 0
    count = k
    while count:
        ans[posx][posy] = "1"
        count -= 1
        if (k - count) % n != 0:
            posx = (posx + 1) % n
            posy = (posy + 1) % n
        else:
            posx = (posx + 1) % n
            posy = (posy + 2) % n

    res = 0
    R = [sum(int(ans[i][j]) for j in range(n)) for i in range(n)]
    C = [sum(int(ans[i][j]) for i in range(n)) for j in range(n)]
    res = (max(R) - min(R))**2 + (max(C) - min(C))**2
    print(res)
    for i in range(n):
        print("".join(ans[i]))
