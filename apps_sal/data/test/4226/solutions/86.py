x, y = list(map(int,input().split()))
cnt = 0
for a in range(x + 1):
    b = x - a
    if b >= 0 and 2 * a + 4 * b == y:
        ans = 'Yes'
        break
else:
    ans = 'No'

print(ans)


