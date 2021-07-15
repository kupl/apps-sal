n = int(input())

shows = []

for i in range(n):
    shows.append(list([int(s) for s in input().split()]))

shows = sorted(shows)

t = [-1,-1]
violate = False

for s in shows:
    if s[0] > t[0]:
        t[0] = s[1]
    elif s[0] > t[1]:
        t[1] = s[1]
    else:
        violate = True
        break

if not violate:
    print('YES')
else:
    print('NO')


