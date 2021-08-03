3

(n, p) = tuple(map(int, input().split()))
buyers = list()
for i in range(n):
    buyers.append(input())
total = 0
money = 0
for i in range(n - 1, -1, -1):
    if buyers[i] == 'halfplus':
        total = (total + 0.5) * 2
        money += p * total * 0.5
    else:
        total = total * 2
        money += p * total * 0.5
print(str(int(money)))
