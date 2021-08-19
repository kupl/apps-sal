def solution(games):
    current_players = [True, True, False]
    for winner in games:
        if not current_players[winner - 1]:
            return False
        current_players = [True if winner - 1 == player else not current_players[player] for player in range(3)]
    return True


n = int(input())
games = [int(input()) for i in range(n)]
print('YES' if solution(games) else 'NO')
