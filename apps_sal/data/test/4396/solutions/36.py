n = int(input())
xu = [list(input().split()) for _ in range(n)]
money = 0
for k in xu:
    if k[1] == 'JPY':
        money += float(k[0])
    else:
        money += float(k[0]) * 380000
print(money)
