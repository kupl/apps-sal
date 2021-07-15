import sys

input = sys.stdin.readline

bingo = []
for _ in range(3):
    bingo.append(list(map(int, input().split())))

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

for num in nums:
    for i in range(3):
        for j in range(3):
            if bingo[i][j] == num:
                bingo[i][j] = -1

for i in range(3):
    if sum(bingo[i]) == -3:
        print("Yes")
        return
    tmp = 0
    for j in range(3):
        tmp += bingo[j][i]
    if tmp == -3:
        print("Yes")
        return
if bingo[0][0] == -1 and bingo[1][1] == -1 and bingo[2][2] == -1:
    print("Yes")
    return
if bingo[0][2] == -1 and bingo[1][1] == -1 and bingo[0][2] == -1:
    print("Yes")
    return

print("No")
