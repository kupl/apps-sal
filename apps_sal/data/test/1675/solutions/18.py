import sys


def main():
    line_num = 0
    teams_num = 0
    teams_per_color = {}
    teams = []
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
    for i in range(0, teams_num):
        away_color = teams[i][1]
        result = (teams_num - 1 + teams_per_color.get(away_color, 0),
                  teams_num - 1 - teams_per_color.get(away_color, 0))
        print("{} {}".format(result[0], result[1]))


def __starting_point():
    main()


__starting_point()
