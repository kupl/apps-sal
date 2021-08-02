n = int(input())
home = {}
guest = []

for i in range(n):
    h, g = [int(c) for c in input().split()]
    home[h] = 1 if not(h in home) else home[h] + 1
    guest.append(g)

for i in range(n):
    h = (n - 1) + (0 if not(guest[i] in home) else home[guest[i]])
    print('%s %s' % (h, ((n - 1) * 2) - h))
