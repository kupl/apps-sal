n = int(input())
price = [0 for i in range(n)]
req = [0 for i in range(n)]
for i in range(n):
    req[i], price[i] = map(int, input().split())

cur_min = price[0]
ans = 0
for i in range(n):
    cur_min = min([price[i], cur_min])
    ans += cur_min * req[i]
print(ans)
