n = int(input())
bx = list(map(int, input().split()))
bx.sort()
vals = {i: 0 for i in bx}
for i in bx:
    vals[i] += 1
print(max(vals.values()))

