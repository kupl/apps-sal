n = input()
year = int(n)
year += 1
n = list(str(year))
while(not(n.count(n[0]) == n.count(n[1]) == n.count(n[2]) == n.count(n[3]) == 1)):
    year += 1
    n = list(str(year))

print(year)
