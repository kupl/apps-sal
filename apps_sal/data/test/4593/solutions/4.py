x = int(input())
# p >= 2, b >= 1
if x == 1:
    ans = 1
else:
    ans = 0
    for i in range(1, x + 1):
        for j in range(2, x + 1):
            e = i**j
            if e <= x:
                ans = max(ans, e)
            else:
                break
print(ans)
