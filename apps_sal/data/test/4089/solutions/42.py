n = int(input())
l = []
while n:
    n -= 1
    l.insert(0, chr(97 + n % 26))
    n //= 26
print(''.join(l))
