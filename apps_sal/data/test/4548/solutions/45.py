(n, m, x) = map(int, input().split())
List = [int(i) for i in input().split()]
lcost = 0
rcost = 0
for a in List:
    if a < x:
        lcost += 1
for b in List:
    if b > x:
        rcost += 1
print(min(lcost, rcost))
