
X = int(input())

pv = 100

r = 0.01

year = 0

while pv < X:
    pv = pv + pv // 100
    year += 1

print(year)
