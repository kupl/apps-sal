from math import ceil


def problem(line1, line2, line3):
    in1 = list(map(int, line1.split()))

    n = in1[0]
    position = in1[1]

    standings = list(map(int, line2.split()))
    awards = list(map(int, line3.split()))

    if n == 1 or position == 1:
        return 1

    my_points = standings[position - 1]
    my_award = awards[0]
    diffs = []

    for index, p in enumerate(reversed(standings[0:position - 1])):
        diffs.append(p - my_points)

    enemies = position - 1
    awards = awards[-(enemies):]

    enemy_idx = 0
    award_idx = 0
    overtakes = 0

    while award_idx < len(awards):
        while (award_idx < enemies) and (diffs[enemy_idx] + awards[award_idx] > my_award):
            award_idx += 1

        if (award_idx < enemies) and (diffs[enemy_idx] + awards[award_idx] <= my_award):
            overtakes += 1
            enemy_idx += 1
            award_idx += 1
        else:
            break

    return position - overtakes


def __starting_point():
    line1 = input()
    line2 = input()
    line3 = input()

    result = problem(line1, line2, line3)

    print(result)


__starting_point()
