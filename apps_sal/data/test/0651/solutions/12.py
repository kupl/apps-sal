import itertools

r, c = input().split()
r, c = int(r), int(c)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def is_valid(k, r, c):
    return (0 <= k[0] < r) and (0 <= k[1] < c)


m = [input() for x in range(r)]

for a in range(r):
    for b in range(c):
        if m[a][b] == 'S':
            start = (a, b)
        elif m[a][b] == 'E':
            end = (a, b)

d = input()
t = 0

for p in itertools.permutations([(0, 1), (0, -1), (-1, 0), (1, 0)]):
    poss = True
    curr = start

    for i in d:
        curr = add(curr, p[int(i)])

        if (curr == end):
            break

        if (is_valid(curr, r, c)) and (m[curr[0]][curr[1]] != '#'):
            continue

        poss = False
        break

    if poss and (curr == end):
        t += 1

print(t)
