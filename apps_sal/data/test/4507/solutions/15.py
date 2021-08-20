from audioop import reverse
(n, m, k) = list(map(int, input().split()))
price = list(map(int, input().split()))
offer = [0] * (k + 1)
for i in range(m):
    (x, y) = list(map(int, input().split()))
    if x <= k:
        offer[x] = max(offer[x], y)
price.sort()
for _ in range(n - k):
    price.pop()
price.sort(reverse=True)
prep = [0] * (k + 1)
for i in range(k):
    prep[i + 1] = prep[i] + price[i]
min_price = [prep[k]] * (k + 1)
min_price[0] = 0
for i in range(k):
    min_price[i + 1] = min(min_price[i + 1], min_price[i] + price[i])
    for j in range(1, k + 1):
        if offer[j] == 0:
            continue
        if i + j > k:
            break
        min_price[i + j] = min(min_price[i + j], min_price[i] + prep[i + j - offer[j]] - prep[i])
print(min_price[k])
