x = int(input())
ans = 1
for i in range(2, int(x ** 0.5) + 1):
    k = 1
    temp = 1
    while temp <= x:
        ans = max(ans, temp)
        temp = i ** k
        k += 1
print(ans)
