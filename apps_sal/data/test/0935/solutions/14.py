(n, m) = map(int, input().split())
a = True
M = False
s = ''
while n != 0 and m != 0:
    if a == True and M == False:
        s = 'Akshat'
        n -= 1
        m -= 1
        a = False
        M = True
    else:
        s = 'Malvika'
        n -= 1
        m -= 1
        a = True
        M = False
print(s)
