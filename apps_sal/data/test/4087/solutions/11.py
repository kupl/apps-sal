a = input()
b = int(a)
while True:
    su  = 0
    a = str(b)
    for i in a:
        su += int(i)
    if su % 4 == 0:
        print(b)
        break
    else:
        b += 1

