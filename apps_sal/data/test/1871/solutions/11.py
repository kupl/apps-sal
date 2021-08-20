(n, x) = [int(c) for c in input().split()]
disc = [int(c) for c in input().split()]
disc.sort()
res = 0
for i in range(len(disc)):
    res += disc[i] * x
    if x > 1:
        x -= 1
print(res)
