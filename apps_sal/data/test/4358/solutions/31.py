N = int(input())
present = []
for i in range(N):
    price = int(input())
    present.append(price)
present.sort(reverse=True)
max_price = present.pop(0)
ans = max_price // 2 + sum(present)
print(ans)
