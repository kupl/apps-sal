n = int(input())
ans = 1
for i in range(1, n):
    if i ** 2 > n:
        ans = (i - 1) ** 2
        break
print(ans)
