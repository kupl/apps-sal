n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]


pot_starts = []
pot_ends = []

for i in a:
    if i[0] == 1:
        pot_starts.append(i[1])
    elif i[1] == n:
        pot_ends.append(i[0])

if set(pot_starts).intersection(pot_ends):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
