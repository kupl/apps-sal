n = int(input())
a = list(map(int, input().split()))
num_map = dict()
for i in range(n):
    if a[i] not in num_map:
        num_map[a[i]] = 1
    else:
        num_map[a[i]] += 1

keys = sorted(list(num_map.keys()), reverse=True)

two_over = []
counter = 0
res = 1
for i in keys:
    if num_map[i] >= 4:
        res *= i ** (2 - counter)
        counter += 2
    elif num_map[i] >= 2:
        counter += 1
        res *= i
    if counter >= 2:
        print(res)
        break
else:
    print((0))
