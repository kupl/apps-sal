def read():
    return list(map(int, input().split()))


(a, b, c) = read()
if c == 0 and b == a:
    ans = 'YES'
elif c != 0 and (b - a) % c == 0:
    if c > 0 and b >= a:
        ans = 'YES'
    elif c < 0 and b <= a:
        ans = 'YES'
    else:
        ans = 'NO'
else:
    ans = 'NO'
print(ans)
