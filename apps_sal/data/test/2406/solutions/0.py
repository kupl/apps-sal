n = int(input())
tot = sum(map(int, input().split()))
extra = (n * (n - 1)) // 2
smol = (tot - extra) // n
out = [smol + i for i in range(n)]
for i in range(tot - sum(out)):
    out[i] += 1
print(' '.join(map(str, out)))
