n = int(input())
cake = [input() for i in range(n)]
cake2 = [[0] * n for i in range(n)]
cakex = [0] * n
cakey = [0] * n
for i in range(n):
    for j in range(n):
        if cake[i][j] == "C":
            cake2[i][j] = 1
            cakex[i] += 1
            cakey[j] += 1

num = 0
for i in range(n):
    num += cakex[i] * (cakex[i] - 1) // 2
    num += cakey[i] * (cakey[i] - 1) // 2
print(num)
