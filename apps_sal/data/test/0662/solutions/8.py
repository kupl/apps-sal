n = int(input())
players = [1, 2]
nub = 3
for i in range(n):
    a = int(input())
    if a in players:
        if players[0] == a:
            b = nub
            nub = players[1]
            players = [a, b]
        else:
            b = nub
            nub = players[0]
            players = [a, b]
    else:
        print('NO')
        break
else:
    print('YES')
