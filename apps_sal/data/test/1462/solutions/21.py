(n, k) = list(map(int, input().split()))
s = input()
count = {}
for c in s:
    count[c] = count.get(c, 0) + 1
a = sorted(list(count.values()), reverse=True)
coins = 0
for c in a:
    if c >= k:
        coins += k * k
        break
    coins += c * c
    k -= c
print(coins)
