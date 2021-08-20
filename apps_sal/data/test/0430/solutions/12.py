n = int(input())
cost = list(map(int, input().split()))
sum = 0
for a in cost:
    sum += a
if cost.count(100) > 0 and cost.count(100) % 2 == 0 or sum % 400 == 0:
    print('YES')
else:
    print('NO')
