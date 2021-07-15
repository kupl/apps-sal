n = int(input())
for i in range(n):
    t = input()
    t = list(t.split())
    a = int(t[0])
    b = int(t[1])
    if (a > b):
        (a , b) = (b , a)
    count = 0
    while (a != 0 and b != 0):
        count += b // a
        b %= a
        if (a > b):
            (a , b) = (b , a)
    print (count)

