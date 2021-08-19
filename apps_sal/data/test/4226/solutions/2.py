(x, y) = map(int, input().split())
ans = 'No'
for i in range(x + 1):
    tmp = 2 * i + 4 * (x - i)
    if tmp == y:
        ans = 'Yes'
print(ans)
