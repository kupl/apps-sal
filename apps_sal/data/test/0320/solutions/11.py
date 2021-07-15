n = int(input())
dominos = [list(map(int, input().split())) for i in range(n)]
sum_1 = 0
sum_2 = 0
ind = False
for i in range(n):
    sum_1 += dominos[i][0] % 2
    sum_1 %= 2
    sum_2 += dominos[i][1] % 2
    sum_2 %= 2
    if dominos[i][1] % 2 != dominos[i][0] % 2:
        ind = True
if sum_1 == sum_2 == 1 and ind:
    print(1)
elif sum_1 == sum_2 == 0:
    print(0)
else:
    print(-1)
