n = int(input())
a = sorted(((value, i) for i, value in enumerate(map(int, input().split()))), reverse=True)

all_sum = sum(value for value, _ in a)

results = []
for i in range(n):
    index = 0 if i > 0 else 1
    if all_sum - a[i][0] == 2 * a[index][0]:
        results.append(a[i][1] + 1)

print(len(results))
if results:
    print(*results, sep=' ')

