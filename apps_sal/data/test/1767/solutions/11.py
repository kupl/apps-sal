n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
s = [a[i] + b[i] for i in range(n)]

max = None
for l in range(0, n):
    aa = a[l]
    bb = b[l]
    for r in range(l, n):
        aa |= a[r]
        bb |= b[r]
        if not max or max < aa+bb:
            max = aa + bb
print(max)

