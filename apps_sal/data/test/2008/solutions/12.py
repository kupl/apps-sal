lines = int(input())

data = []
for i in range(lines):
    l, r = list(map(int, input().split(' ')))
    data.append((l, r))

data = sorted(data, key=lambda x: x[1] - x[0])

t = 0
for i, (l, r) in enumerate(data):
    t += l * i + r * (lines - i - 1)

print(t)
