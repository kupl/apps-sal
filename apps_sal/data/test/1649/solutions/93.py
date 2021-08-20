(a, b, c, d) = map(int, input().split())
sum = a + b + c + d
ans = 'No'
if a == sum - a or b == sum - b or c == sum - c or (d == sum - d):
    ans = 'Yes'
if a + b == c + d or a + c == b + d or a + d == b + c:
    ans = 'Yes'
print(ans)
