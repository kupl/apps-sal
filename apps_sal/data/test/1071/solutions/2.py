import math
sa = input().split(' ')
sa2 = input().split(' ')
sa3 = int(input())
cups = [int(x) for x in sa]
medals = [int(x) for x in sa2]
if math.ceil(sum(cups) / 5) + math.ceil(sum(medals) / 10) > sa3:
    print('NO')
else:
    print('YES')
