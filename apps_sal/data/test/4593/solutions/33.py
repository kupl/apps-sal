x = int(input())
ans = 0
if x <= 2:
    ans = x
else:
    for i in range(1, x + 1):
        for j in range(2, x + 1):
            if i ** j <= x:
                ans = max(ans, i ** j)
            elif i ** j > x:
                break
print(ans)
