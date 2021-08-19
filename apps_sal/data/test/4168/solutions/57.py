n = int(input())
amari = []
while True:
    if n > 1 or n < 0:
        amari.append(-(n % -2))
        n = (n - -(n % -2)) // -2
    else:
        amari.append(n)
        break
gyaku = amari[::-1]
print(*gyaku, sep='')
