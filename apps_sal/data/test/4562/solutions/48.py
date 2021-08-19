n = int(input())
ans = 1
loop = 3
for i in range(1, 100000):
    if i ** 2 <= n:
        ans = i ** 2
print(ans)
