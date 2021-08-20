n = int(input())
x = [int(i) for i in input().split()]
hp = []
for p in range(min(x), max(x) + 1):
    sum = 0
    for i in x:
        sum = sum + (i - p) ** 2
    hp.append(sum)
print(min(hp))
