n = int(input())
al = 'abcdefghijklmnopqrstuvwxyz'
s = ''
while n:
    n -= 1
    e = n % 26
    s = al[e] + s
    n //= 26
print(s)
