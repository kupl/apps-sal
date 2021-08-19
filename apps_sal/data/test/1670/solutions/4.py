(team1, team2) = (input(), input())
n = int(input())
yellow = set()
red = set()
for i in range(n):
    (a, b, c, d) = input().split()
    a = int(a)
    c = int(c)
    c2 = c
    if b != 'h':
        c += 111000
    if d == 'y':
        if c in red:
            continue
        if c in yellow:
            print(team1 if b == 'h' else team2, c2, a)
            red.add(c)
        else:
            yellow.add(c)
    if d == 'r':
        if c in red:
            continue
        print(team1 if b == 'h' else team2, c2, a)
        red.add(c)
