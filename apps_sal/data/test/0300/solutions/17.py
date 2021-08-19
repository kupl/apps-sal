n = int(input())
tab = sorted([int(x) for x in input().split()])
s = sum(tab)
result = 0
for i in range(n):
    if 2 * s >= 9 * n:
        break
    result += 1
    s -= tab[i]
    s += 5
print(result)
