(a, b, x) = map(int, input().split())
if a <= x and a + b >= x:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)
