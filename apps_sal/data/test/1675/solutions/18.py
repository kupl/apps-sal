import sys


def main():
    line_num = 0
    teams_num = 0
    teams_per_color = {}
    teams = []
    # read input data
    for line in sys.stdin:
        if line_num == 0:
            teams_num = int(line.strip())
        elif line_num <= teams_num:
            res = list([int(x) for x in line.strip().split(' ')])
            if res[0] not in teams_per_color:
                teams_per_color[res[0]] = 0
            teams_per_color[res[0]] = teams_per_color[res[0]] + 1
            teams.append((res[0], res[1]))
        line_num += 1
        if line_num > teams_num:
            break
    # - if 1 color belongs to 1 team only -> there will be no problems with this
    # team and this team will wear this color during all games of one type.
    # - if all teams that wear this color have one kit_type (all play away
    # games in this color, for example, then there will be no problems, as
    # we don't have away-away team problem)
    # - otherwise have to calculate 'delta': times when need to change AWAY
    # kit to HOME one
    for i in range(0, teams_num):
        # if away color is shared among some home-teams, then have to change
        away_color = teams[i][1]
        result = (teams_num - 1 + teams_per_color.get(away_color, 0),
                  teams_num - 1 - teams_per_color.get(away_color, 0))
        print("{} {}".format(result[0], result[1]))

def __starting_point():
    main()

__starting_point()
