n = int(input())
l = []
s = 12
for i in range(n):
    y = input()
    s = min({sum((a != b for (a, b) in zip(x, y))) - 1 for x in l} | {s})
    l += [y]
print(s // 2)
