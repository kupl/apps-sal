n, t = (int(i) for i in input().split())
portals = [int(i) for i in input().split()]
home = 1
while True:
    if home == t:
        print('YES')
        break
    elif home > t:
        print('NO')
        break
    home += portals[home - 1]
