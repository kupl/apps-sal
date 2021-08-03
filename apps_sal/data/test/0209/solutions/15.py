x, y = list(map(int, input().split()))
n = int(input())


def modulo(a):
    if a == 1000000007:
        return 0
    elif a >= 0:
        return int(a % (1000000007))
    else:
        if a % 1000000007 == 0:
            return 0
        else:
            return int((1000000007) - int(((-1) * a) % (1000000007)))


n = n % 6
if n == 1:
    print(modulo(x))
elif n == 2:
    print(modulo(y))
elif n == 3:
    print(modulo(y - x))
elif n == 4:
    print(modulo(-x))
elif n == 5:
    print(modulo(-y))
elif n == 0:
    print(modulo(x - y))
