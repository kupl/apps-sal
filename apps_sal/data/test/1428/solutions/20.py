(n, c) = list(map(int, input().split()))
diff = [list(map(int, input().split())) for _ in range(c)]
color = [list(map(int, input().split())) for _ in range(n)]
dic = [[0] * c for _ in range(3)]
for i in range(n):
    for j in range(n):
        dic[(i + j) % 3][color[i][j] - 1] += 1
result = 10 ** 9
for aa in range(c):
    a_cost = 0
    for j in range(c):
        a_cost += dic[0][j] * diff[j][aa]
    for bb in range(c):
        if aa != bb:
            b_cost = 0
            for j in range(c):
                b_cost += dic[1][j] * diff[j][bb]
            for cc in range(c):
                if aa != bb and bb != cc and (cc != aa):
                    c_cost = 0
                    for j in range(c):
                        c_cost += dic[2][j] * diff[j][cc]
                    result = min(result, a_cost + b_cost + c_cost)
print(result)
