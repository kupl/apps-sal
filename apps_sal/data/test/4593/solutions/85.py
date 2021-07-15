x = int(input())
ans = 1
for p in range(2, x+1):
    for b in range(1, x+1):
        if b**p <= x:
            ans = max(ans, b**p)
        else:
            break
print(ans)
