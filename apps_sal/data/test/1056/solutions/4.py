links = list(range(100))
# 0 0 = left up
# 10*y+x

# i = height
# j = pos
for i in range(10):
    l = list(map(int, input().split()))
    for j, h in enumerate(l):
        coo = i * 10 + (j if i % 2 == 0 else 9 - j)
        target = (i - h) * 10 + (j if (i - h) % 2 == 0 else 9 - j)
        links[coo] = target

exp = [0]
for i in range(1, 6):
    exp.append((1 + sum(exp) * 1 / 6) * 6 / i)

for i in range(6, 100):
    new = 0
    for j in range(1, 7):
        new += min(exp[i - j], exp[links[i - j]])
    exp.append(1 + new / 6)

print(exp[-1])
