n = int(input())
s = ''
while True:
    if n % 2 == 0:
        s = '0' + s
        n = n // -2
    else:
        s = '1' + s
        n = (n - 1) // -2
    if n == 0:
        break
print(s)
