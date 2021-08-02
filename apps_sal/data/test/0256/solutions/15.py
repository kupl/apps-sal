def find_winer(defence1, attack1, defence2, attack2):
    if defence1[0] > attack2[1] and attack1[1] > defence2[0]:
        return 1
    elif defence1[0] < attack2[1] and attack1[1] < defence2[0]:
        return 2
    else:
        return 0


def find_results(players):
    results = []
    results.append(find_winer(players[0], players[1], players[2], players[3]))
    results.append(find_winer(players[0], players[1], players[3], players[2]))
    results.append(find_winer(players[1], players[0], players[2], players[3]))
    results.append(find_winer(players[1], players[0], players[3], players[2]))

    return results


def solve():
    players = []
    for i in range(4):
        players.append(tuple(map(int, input().split())))

    results = find_results(players)
    if (results[0] == 1 and results[1] == 1) or (results[2] == 1 and results[3] == 1):
        print("Team 1")
    elif (results[0] == 2 or results[1] == 2) and (results[2] == 2 or results[3] == 2):
        print("Team 2")
    else:
        print("Draw")


solve()
