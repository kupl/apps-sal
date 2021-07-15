n = int(input())

local = [0]*(10**5+1)

kits = []

for i in range(n):
    x, y = list(map(int, input().split(" ")))
    kits.append((x, y))
    local[x] += 1

res = ["%s %s" % (n-1+local[y], n-1-local[y]) for (x, y) in kits]

print("\n".join(res))
