mod = 10**9 + 7

n = int(input())

a = sorted(map(int, input().split()))
ma = max(a)

prev = -1
smaller = 0
cur = 0
total = 0
for x in a:
    if x == ma:
        continue

    if x == prev:
        cur += 1
    else:
        smaller += cur
        cur = 1
        prev = x

    total += x * pow(n - smaller, mod - 2, mod)
    total %= mod


for i in range(1, n + 1):
    total *= i
    total %= mod
print(total)
