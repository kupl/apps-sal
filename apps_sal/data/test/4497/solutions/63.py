n = int(input())
ans = 0
for i in range(7):
    if (n >> i) & 1:
        ans = (n >> i) << i
print(ans)
