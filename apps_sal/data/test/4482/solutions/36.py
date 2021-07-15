N = int(input())
a = list(map(int, input().split()))
s = sum(a)
x = int(s / len(a))

if (x + 1) - (s / len(a)) < (s / len(a)) - x:
    x += 1
cost = 0
for y in a:
    cost += pow(y - x, 2)

print(cost)
