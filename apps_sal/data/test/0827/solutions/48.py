import sys
n = int(input())
t = input()

if t == '0':
    print((10**10))
elif t == '1':
    print((2*(10**10)))
else:
    s = 0
    e = 0
    if t[:2] == '11':
        s = 0
    elif t[:2] == '10':
        s = 1
    elif t[:2] == '01':
        s = 2
    else:
        print((0))
        return
    
    check = '110'
    e = s + n - 1
    
    for i in range(2,n):
        if t[i] != check[(i+s)%3]:
            print((0))
            return

    print(((3 * (10 ** 10) -1 - e) // 3+1))

