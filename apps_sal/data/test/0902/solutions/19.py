# python3
# utf-8

players_nr, max_win_streak = (int(x) for x in input().split())
player_idx___power = [int(x) for x in input().split()]
if max_win_streak > players_nr:
    print(max(player_idx___power))
    quit()
curr_win_streak = 0
curr_power = player_idx___power[0]
next_player_idx = 1
while curr_win_streak < max_win_streak:
    next_power = player_idx___power[next_player_idx]
    if curr_power < next_power:
        curr_power = next_power
        player_idx___power.append(curr_power)
        curr_win_streak = 1
    else:
        player_idx___power.append(next_power)
        curr_win_streak += 1
    next_player_idx += 1
print(curr_power)

