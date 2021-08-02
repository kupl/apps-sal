n, m = list(map(int, input().split()))

games = list(map(int, input().split()))

moneys = list(map(int, input().split()))

answer = 0

game_ind = 0
money_ind = 0


while game_ind < n and money_ind < m:

    if moneys[money_ind] >= games[game_ind]:
        answer += 1
        game_ind += 1
        money_ind += 1
    else:
        game_ind += 1

print(answer)
