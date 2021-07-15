n, m = list(map(int, str.split(input())))
teams = 0
while n and m and n + m > 2:

    if n >= m and n > 1:

        teams, n, m = teams + 1, n - 2, m - 1

    elif m > 1:

        teams, n, m = teams + 1, n - 1, m - 2

print(teams)

