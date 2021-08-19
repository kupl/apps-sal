x = int(input())
ans = 1
for i in range(1, x + 1):
    for j in range(2, 11):
        if i ** j <= x:
            ans = max(ans, i ** j)
        else:
            break
print(ans)
