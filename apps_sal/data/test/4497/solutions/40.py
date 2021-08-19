n = int(input())
ans = 1
for i in range(1, 7):
    if 2 ** i <= n:
        ans = 2 ** i
print(ans)
