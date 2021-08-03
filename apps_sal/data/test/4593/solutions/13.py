n = int(input())
ans = 1
for i in range(1, n):
    for j in range(2, n):
        if i ** j <= n:
            ans = max(ans, i ** j)
        else:
            break
print(ans)
