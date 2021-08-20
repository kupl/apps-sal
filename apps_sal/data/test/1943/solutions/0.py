import functools
n = int(input())
props = []


def preproc(a):
    return float(a) / 100.0


for i in range(pow(2, n)):
    props.append(list(map(preproc, input().split())))
wining_props = []
wining_props_first_round = []
for i in range(0, 2 ** n, 2):
    wining_prop_for_i = props[i][i + 1]
    wining_props_first_round.append(wining_prop_for_i)
    wining_props_first_round.append(1.0 - wining_prop_for_i)
wining_props.append(wining_props_first_round)
assert len(wining_props_first_round) == len(props)
for round_num in range(2, n + 1):
    this_round_wining_props = []
    for team_num in range(2 ** n):
        t = team_num // 2 ** round_num * 2 ** round_num
        teams_we_meet_this_round = [t + x for x in range(2 ** round_num)]
        t = team_num // 2 ** (round_num - 1) * 2 ** (round_num - 1)
        teams_we_meet_prev_round = [t + x for x in range(2 ** (round_num - 1))]
        for tt in teams_we_meet_prev_round:
            teams_we_meet_this_round.remove(tt)
        this_team_wining_props = wining_props[round_num - 2][team_num]
        chances_win_i_team = []
        for tm in teams_we_meet_this_round:
            chances_win_i_team.append(wining_props[round_num - 2][tm] * props[team_num][tm])
        mo_win_this_round = sum(chances_win_i_team)
        this_team_wining_props *= mo_win_this_round
        this_round_wining_props.append(this_team_wining_props)
    wining_props.append(this_round_wining_props)


@functools.lru_cache(maxsize=None)
def revenue(round_num, teams_left, teams_right, winner=-1):
    split = (teams_left + teams_right) // 2
    if round_num == 1:
        return wining_props[0][winner] if winner != -1 else max(wining_props[0][teams_left:teams_right])
    if winner == -1:
        results = []
        for winner in range(teams_left, teams_right):
            winner_prop = wining_props[round_num - 1][winner]
            if winner >= split:
                res = sum([revenue(round_num - 1, teams_left, split), revenue(round_num - 1, split, teams_right, winner), winner_prop * 2 ** (round_num - 1)])
            else:
                res = sum([revenue(round_num - 1, teams_left, split, winner), revenue(round_num - 1, split, teams_right), winner_prop * 2 ** (round_num - 1)])
            results.append(res)
        return max(results)
    else:
        winner_prop = wining_props[round_num - 1][winner]
        if winner >= split:
            res = sum([revenue(round_num - 1, teams_left, split), revenue(round_num - 1, split, teams_right, winner), winner_prop * 2 ** (round_num - 1)])
        else:
            res = sum([revenue(round_num - 1, teams_left, split, winner), revenue(round_num - 1, split, teams_right), winner_prop * 2 ** (round_num - 1)])
        return res


print(revenue(n, 0, 2 ** n))
