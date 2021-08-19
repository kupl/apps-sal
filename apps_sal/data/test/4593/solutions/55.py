x = int(input())
ans = 1
for i in range(x):
    for j in range(2, 10):
        if i ** j <= x:
            ans = max(ans, i ** j)
        else:
            break
print(ans)
