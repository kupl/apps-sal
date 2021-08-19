count = 0
n = int(input())
for i in range(n):
    dice = input().split()
    if dice[0] == dice[1]:
        count += 1
    else:
        count = 0
    if count == 3:
        break
if count == 3:
    print('Yes')
else:
    print('No')
