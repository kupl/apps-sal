number = int(input())
doublets = 0
for i in range(number):
    (dice1, dice2) = list(map(int, input().split()))
    if dice1 == dice2:
        doublets += 1
    else:
        doublets = 0
    if doublets == 3:
        break
if doublets == 3:
    print('Yes')
else:
    print('No')
