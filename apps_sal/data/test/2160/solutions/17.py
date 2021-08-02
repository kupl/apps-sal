n, k = map(int, input().split())
X = list(map(int, input().split()))

fallen = set()
pairs = set()

for x in X:
    if (x - 1) in fallen:
        #pairs.add([x-1, x])
        pairs.add((x - 1) * (n + 1) + x)
    if (x + 1) in fallen:
        #pairs.add([x+1, x])
        pairs.add((x + 1) * (n + 1) + x)
    fallen.add(x)

print(2 * (n - 1) + n - len(pairs) - len(fallen))
