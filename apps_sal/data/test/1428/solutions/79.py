from itertools import permutations
n, c = map(int, input().split())

d_lst = [list(map(int, input().split())) for _ in range(c)]
c_lst = [list(map(int, input().split())) for _ in range(n)]

lst = [[0] * c for _ in range(3)]

for i in range(n):
    for j in range(n):
        lst[(i + j) % 3][c_lst[i][j] - 1] += 1

cnt = []

for i in range(c):
    temp = []
    for j in range(3):
        cal = 0
        for k in range(c):
            cal += lst[j][k] * d_lst[k][i]
        temp.append(cal)
    cnt.append(temp)


temp = []
for l in permutations(list(range(c)), 3):
    temp.append(cnt[l[0]][0] + cnt[l[1]][1] + cnt[l[2]][2])

print(min(temp))
