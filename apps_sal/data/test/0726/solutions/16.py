(n, d) = map(int, input().strip().split())
city = list(map(int, input().strip().split()))
count = 2
for i in range(1, n):
    if city[i] - city[i - 1] == 2 * d:
        count = count + 1
    elif city[i] - city[i - 1] > 2 * d:
        count = count + 2
    else:
        continue
print(count)
