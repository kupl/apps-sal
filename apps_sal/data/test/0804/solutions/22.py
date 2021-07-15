word = input()
n = int(input())

ns = {}


for c in word:
    if not c in ns.keys():
        ns[c] = 1
    else:
        ns[c] += 1

# d = max(0, n - len(ns))

# foo = list(filter(lambda i: i > 0, map(lambda x: x-1, ns.values())))

if len(word) >= n:
    print(max(0, n - len(ns)))
else:
    print("impossible")
