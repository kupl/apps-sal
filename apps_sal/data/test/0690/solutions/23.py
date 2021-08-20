n = int(input())


def numofdigits(n):
    ans = 0
    while n > 0:
        ans += 1
        n = n // 10
    return ans


rods = numofdigits(n)


def whattoprint(n):
    if n == 0:
        return 'O-|-OOOO'
    elif n == 1:
        return 'O-|O-OOO'
    elif n == 2:
        return 'O-|OO-OO'
    elif n == 3:
        return 'O-|OOO-O'
    elif n == 4:
        return 'O-|OOOO-'
    elif n == 5:
        return '-O|-OOOO'
    elif n == 6:
        return '-O|O-OOO'
    elif n == 7:
        return '-O|OO-OO'
    elif n == 8:
        return '-O|OOO-O'
    else:
        return '-O|OOOO-'


if n == 0:
    print('O-|-OOOO')
for i in range(rods):
    num = n % 10
    n = n // 10
    ans = whattoprint(num)
    print(ans)
