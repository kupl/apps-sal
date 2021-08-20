n = int(input())
alf = '0abcdefghijklmnopqrstuvwxyz'
ans = ''
while n != 0:
    x = n % 26
    if x == 0:
        x = 26
    ans += alf[x]
    n -= x
    n //= 26
print(ans[::-1])
