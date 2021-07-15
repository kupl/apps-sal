t = int(input())
ns = []
for _ in range(t):
    n = int(input())
    ns.append(n)

for n in ns:
    print(2)
    print(n-1, n)
    if n > 2:
        for x in range(n, 2, -1):
            print(x-2, x)

