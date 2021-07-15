3

def readln(): return tuple(map(int, input().split()))

def tostr(d):
    if d >= 5:
        return '-O|' + 'O' * (d % 5) + '-' + 'O' * (4 - d % 5)
    return 'O-|' + 'O' * d + '-' + 'O' * (4 - d)

n, = readln()
if n == 0:
    print('O-|-OOOO')
else:
    while n:
        print(tostr(n % 10))
        n //= 10

