
n, k = list(map(int, input().split()))

tab = [int(x) for x in input().split()]

best = 1

for i in tab:
    if k % i == 0:
        best = max([i, best])

print(k // best)

