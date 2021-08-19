n = int(input())
meat = [0] * n
price = [0] * n
for i in range(n):
    (meat[i], price[i]) = list(map(int, input().split()))
min_price = price[0]
ans = 0
for i in range(n):
    min_price = min(min_price, price[i])
    ans += min_price * meat[i]
print(ans)
