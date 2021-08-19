(x, y) = list(map(int, input().split()))
ans = 'No'
for a in range(x + 1):
    b = x - a
    if 2 * a + 4 * b == y:
        ans = 'Yes'
print(ans)
