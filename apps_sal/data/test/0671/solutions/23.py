n = int(input())
crt = 1
a = ''
while len(a) < n:
    a += str(crt)
    crt += 1
print(a[n - 1])
