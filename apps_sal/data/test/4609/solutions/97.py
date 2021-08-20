n = int(input())
d = {}
for i in range(n):
    a = int(input())
    if a in d:
        d[a] ^= 1
    else:
        d[a] = 1
print(sum(d.values()))
