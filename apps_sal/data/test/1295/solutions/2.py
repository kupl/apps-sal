n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

class Zona:
    def __init__(self, vis, gran, t):
        self.v = vis
        self.gr = gran
        self.type = t
        self.towns = []
        
zones = []
zones.append(Zona(b[0], -10**9 - 1, 1))
for i in range(0, m - 1):
    gr = (b[i] + b[i+1]) / 2
    zones.append(Zona(b[i], gr, 2))
    zones.append(Zona(b[i+1], gr, 1))
    
zones.append(Zona(b[m - 1], 10**9 + 1, 2))

i = 0
for zone in zones:
    if zone.type == 1:
        while ((a[i] >= zone.gr) and (a[i] < zone.v)):
            zone.towns.append(a[i])
            i += 1
            if (i == n): break
    if zone.type == 2:
        while (a[i] >= zone.v) and (a[i] < zone.gr):
            zone.towns.append(a[i])
            i += 1
            if (i == n): break
    if (i == n): break
    
r = 0
for zone in zones:
    for town in zone.towns:
        dist = abs(zone.v - town)
        if (dist > r):
            r = dist
            
print(r)
    

