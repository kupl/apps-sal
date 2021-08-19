(a, b) = map(str, input().split())
if a == 'H':
    if b == 'H':
        ans = 'H'
    else:
        ans = 'D'
elif b == 'H':
    ans = 'D'
else:
    ans = 'H'
print(ans)
