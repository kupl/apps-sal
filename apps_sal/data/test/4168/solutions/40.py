n = int(input())
N = n
ans = ''
while n != 0:
    if n % 2 == 1:
        ans += '1'
        n = n - 1
        n //= -2
    else:
        ans += '0'
        n //= -2
print(ans[::-1] if N != 0 else 0)
