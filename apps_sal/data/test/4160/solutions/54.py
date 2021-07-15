x = int(input())

a = 100

i = 1
while 1:
    a += (a // 100)
    if a >= x:
        print(i)
        return
    i += 1
