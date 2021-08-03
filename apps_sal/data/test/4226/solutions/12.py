x, y = list(map(int, input().split()))

ans = 'No'

for i in range(x + 1):
    j = x - i
    if 2 * i + 4 * j == y:
        ans = 'Yes'
        break

print(ans)
