a = [[x for x in map(int, input().split())] for _ in range(3)]
n = int(input())
bingo = [[0] * 3 for _ in range(3)]
for k in range(n):
    x = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == x:
                bingo[i][j] = 1
for i in range(3):
    if bingo[i] == [1, 1, 1]:
        print('Yes')
        return
    if [row[i] for row in bingo] == [1, 1, 1]:
        print('Yes')
        return
if [bingo[i][i] for i in range(3)] == [1, 1, 1]:
    print('Yes')
    return
if [bingo[i][2 - i] for i in range(3)] == [1, 1, 1]:
    print('Yes')
    return
print('No')
