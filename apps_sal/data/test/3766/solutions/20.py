input()
p = {(1 << 'RGBYW'.index(c)) + (1 << int(k) + 4) for (c, k) in input().split()}
mn = 20
res = 90
for i in range(1024):
    if len(p) == len(set((i & j for j in p))):
        mn = min(mn, bin(i).count('1'))
print(mn)
