from sys import stdin
rounds = int(stdin.readline())
mis = 0
chris = 0
for i in range(rounds):
    score = list(map(int, stdin.readline().split()))
    if score[0] > score[1]:
        mis += 1
    elif score[0] < score[1]:
        chris += 1
    else:
        mis += 1
        chris += 1
if mis == chris:
    print('Friendship is magic!^^')
elif mis > chris:
    print('Mishka')
else:
    print('Chris')
