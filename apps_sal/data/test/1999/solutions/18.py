n = int(input())
a = [int(x) for x in input().split()]
repeats = {}
for (i, v) in enumerate(a):
    x = v
    while x in repeats:
        del repeats[x]
        x *= 2
    repeats[x] = i
print(len(repeats))
print(*repeats.keys())
