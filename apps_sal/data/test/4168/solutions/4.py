N = int(input())

if N == 0:
    print((0))
    return

ans = ''
while N:
    if N % 2:
        N -= 1
        ans += '1'
    else:
        ans += '0'
    N //= -2

print((ans[::-1]))
