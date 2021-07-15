n, k = list(map(int, input().split()))

ans = 0

price_list = list(map(int, input().split()))
price_list.sort()

for i in range(k):
    ans += price_list[i]

print(ans)

