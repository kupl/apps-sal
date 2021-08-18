input()
num = [4, 8, 15, 16, 23, 42]
prev = {i: j for i, j in zip(num[1:], num)}
c = {v: 0 for v in num}
n = 0
for a in map(int, input().split()):
    if a == num[0]:
        c[a] += 1
    else:
        if c[prev[a]]:
            c[prev[a]] -= 1
            if a != num[-1]:
                c[a] += 1
        else:
            n += 1

for i, v in enumerate(num):
    n += (i + 1) * c[v]

print(n)
