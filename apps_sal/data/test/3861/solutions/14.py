n = int(input())
best = -1000000000
for i in map(int, input().split()):
    if i < 0:
        best = max(best, i)
        continue
    if (i**0.5 != int(i**0.5)):
        best = max(best, i)


print(best)
