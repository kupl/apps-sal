N = int(input())
if N == 0:
    print('0')
    return

ans = ''
while abs(N) > 0:
    if abs(N) % 2 == 0:
        ans += '0'
        N //= 2
    else:
        N -= 1
        N //= 2
        ans += '1'
    N *= -1
print((ans[::-1]))
