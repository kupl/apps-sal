x, y = list(map(int, input().split()))
ans = 'No'
for i in range(x + 1):
    j = x - i
    if i * 2 + j * 4 == y:
        ans = 'Yes'
        break

print(ans)

