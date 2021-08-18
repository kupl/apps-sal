x = int(input())
ans = 0
for i in range(x):
    for j in range(2, 10):
        if i**j <= x:
            ans = max(ans, i**j)
        else:
            break

if ans == 0:
    ans = 1

print(ans)
