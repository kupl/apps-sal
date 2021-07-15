n = int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
while n > 0:
    n -= 1
    ans += s[n%26]
    n //= 26

print(ans[::-1])
