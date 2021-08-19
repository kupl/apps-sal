n = int(input())
a = 'xabcdefghijklmnopqrstuvwxyz'
ans = ''
while True:
    d = n % 26
    if d == 0:
        d = 26
    ans += a[d]
    n -= d
    if n == 0:
        break
    n = n // 26
print(ans[::-1])
