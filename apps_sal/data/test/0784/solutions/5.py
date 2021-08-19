(a, b) = map(int, input().split())
ans = [b]
while b > a:
    if b % 10 == 1:
        b //= 10
        ans += [b]
    elif b % 2 == 0:
        b //= 2
        ans += [b]
    else:
        break
if b == a:
    print('YES')
    print(len(ans))
    ans.reverse()
    print(' '.join(list(map(str, ans))))
else:
    print('NO')
