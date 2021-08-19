(a, b, c, d) = map(int, input().split())
ans = 'No'
if abs(c - a) <= d:
    ans = 'Yes'
elif abs(c - b) <= d and abs(b - a) <= d:
    ans = 'Yes'
print(ans)
