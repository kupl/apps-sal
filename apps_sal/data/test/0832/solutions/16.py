def count_guest_uniform_on_host_team(n_teams: int, home_colours: list, guest_colours: list) -> int:
    result = 0

    for i in range(n_teams):
        result += guest_colours.count(home_colours[i])

    return result

n = int(input())
h = [None] * n
a = [None] * n

for i in range(n):
    h[i], a[i] = map(int, input().split())

print(count_guest_uniform_on_host_team(n, h, a))
