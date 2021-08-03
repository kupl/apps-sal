a = [int(input()) for i in range(6)]
mi = min(a)
if(a[0] == mi):
    print(5)
else:
    if(a[0] % mi == 0):
        print(5 + a[0] // mi - 1)
    else:
        print(5 + a[0] // mi)
