from collections import Counter

n, k = list(map(int, input().split()))
colors = input()

d = Counter(colors)

for color, i in list(d.items()):
    if i > k:
        print('NO')
        break
else:
    print('YES')

