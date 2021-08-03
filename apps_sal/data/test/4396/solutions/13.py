N = int(input())
ans = 0
for _ in range(N):
    x, u = input().split()
    x = float(x)
    if u == "JPY":
        ans += x
    else:
        ans += 380000 * x
print(ans)
