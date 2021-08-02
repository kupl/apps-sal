n = int(input())
ans = 0
k = 1
while k ** 2 <= n:
    ans = k ** 2
    k += 1
print(ans)
