N = int(input())
b_to_y = 380000
ans = 0
for i in range(N):
    p, unit = input().split()
    if unit == "JPY":
        ans += int(p)
    if unit == "BTC":
        ans += (b_to_y * float(p))
print(ans)
