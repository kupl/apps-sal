(a, b, x) = list(map(int, input().split(' ')))
ans = ''
if a > b:
    s = '01'
    ans += s * (x // 2)
    if x % 2 == 0:
        ans += '1' * (b - x // 2)
        ans += '0' * (a - x // 2)
    else:
        ans += '0' * (a - x // 2)
        ans += '1' * (b - x // 2)
else:
    s = '10'
    ans += s * (x // 2)
    if x % 2 == 0:
        ans += '0' * (a - x // 2)
        ans += '1' * (b - x // 2)
    else:
        ans += '1' * (b - x // 2)
        ans += '0' * (a - x // 2)
print(ans)
