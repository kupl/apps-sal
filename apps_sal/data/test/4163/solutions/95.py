N = int(input())
dice = []

for _ in range(N):
    dice.append(list(map(int, input().split())))

check = 3
for n in range(N):
    if dice[n][0] == dice[n][1]:
        check -= 1
        if check == 0:
            print('Yes')
            return
    else:
        check = 3

print('No')

