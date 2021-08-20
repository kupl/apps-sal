amount = int(input())
bet = map(int, input().split())
bet_list = list(bet)
for i in range(0, amount):
    while bet_list[i] % 2 == 0:
        bet_list[i] /= 2
    while bet_list[i] % 3 == 0:
        bet_list[i] /= 3
bet_list.sort()
if max(bet_list) == min(bet_list):
    print('Yes')
else:
    print('No')
