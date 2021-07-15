n,m = map(int, input().split())
ab = []
for i in range(n):
    a,b = list(map(int, input().split()))
    ab.append((a,b))
ab.sort()
num = 0
money = 0
for h in range(n):
    num += ab[h][1]
    if num < m:
        money += ab[h][0]*ab[h][1]
    elif num == m:
        money += ab[h][0]*ab[h][1]
        break
    else:
        money += (ab[h][0]*ab[h][1] - (num-m)*ab[h][0])
        break
print(money)
