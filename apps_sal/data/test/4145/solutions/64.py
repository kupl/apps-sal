x = int(input())


def hantei(x):
    p = []
    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return False
    else:
        return True


while 1:
    if hantei(x):
        print(x)
        break
    else:
        x += 1
