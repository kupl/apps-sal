n, x, y = list(map(int, input().split()))
teams = list(map(int, input().split()))

teams.sort()

c = 0

for team in teams:
    if x:
        pages_to_print = min(team // 2, x)
        x -= pages_to_print
        team -= pages_to_print * 2
    if team:
        if y:
            pages_to_print = min(team, y)
            y -= pages_to_print
            team -= pages_to_print
        if team:
            pages_to_print = sum(divmod(team, 2))
            if pages_to_print > x: break
            x -= pages_to_print
    c += 1

print(c)

