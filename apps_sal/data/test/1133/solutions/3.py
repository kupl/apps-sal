from string import ascii_lowercase
n = int(input())
words = [input() for _ in range(n)]
words = [word for word in words if len(set(word)) <= 2]
best = -1
for i1 in range(25):
    for i2 in range(i1 + 1, 26):
        cs = {ascii_lowercase[i1], ascii_lowercase[i2]}
        cw = [word for word in words if set(word) <= cs]
        cl = sum(len(word) for word in cw)
        if cl > best:
            best = cl
print(best)

