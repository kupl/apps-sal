n = int(input())
jail = False
doubles = 0
for i in range(n):
    dice = input().split()
    if dice[0] == dice[1]:
        doubles += 1
    else:
        doubles = 0
    if doubles == 3:
        jail = True
        print('Yes')
if not jail:
    print('No')
