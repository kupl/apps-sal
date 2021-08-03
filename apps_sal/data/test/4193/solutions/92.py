sheet = []
lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
         [0, 3, 6], [1, 4, 7], [2, 5, 8],
         [0, 4, 8], [2, 4, 6]]
sai = []
for i in range(3):
    sheet += [int(j) for j in input().split()]
n = int(input())
for i in range(n):
    sai.append(int(input()))
ret = 'No'
for line in lines:
    bingo = True
    for l in line:
        if sheet[l] not in sai:
            bingo = False
    if bingo:
        ret = 'Yes'
print(ret)
