q = int(input())
for i in range(q):
    n, m = list(map(int,input().split()))
    field = [input() for j in range(n)]
    raw = [0] * n
    col = [0] * m
    num = 0
    for j in range(n):
        for z in range(m):
            if field[j][z] == "*":
                raw[j] += 1
                col[z] += 1
    for z in range(m):
        for j in range(n):
            temp = raw[j] + col[z] - int(field[j][z] == "*")
            if num < temp:
                num = temp
    print(n + m - num - 1)

