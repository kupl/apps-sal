n, a = list(map(int, input().split()))
if a % 2: ans = a // 2 + 1
else: ans = (n - a) // 2 + 1
print(ans)

