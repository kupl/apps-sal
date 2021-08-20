n = int(input())
x = list(map(int, input().split()))
hp_min = 10000000
for i in range(101):
    hp_min = min(hp_min, sum(((y - i) ** 2 for y in x)))
print(hp_min)
