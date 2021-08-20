n = int(input())
teams = [int(x) for x in input().split()]
res = 'YES'
diff = 0
for team in teams:
    if diff > 0 and team == 0:
        res = 'NO'
        break
    diff = (team + diff) % 2
if res == 'YES' and diff > 0:
    res = 'NO'
print(res)
