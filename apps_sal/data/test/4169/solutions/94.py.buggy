n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
a = sorted(a, key=lambda x: x[0])
money = 0
drink = 0
for i in range(n):
    for j in range(a[i][1]):
        drink += 1
        money += a[i][0]
        if drink == m:
            print(money)
            return
