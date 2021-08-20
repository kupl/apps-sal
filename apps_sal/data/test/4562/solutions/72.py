n = int(input())
ans = 0
max = int(n ** 0.5) + 1
for i in range(1, max, 1):
    tmp = i ** 2
    if tmp <= n:
        ans = tmp
print(ans)
