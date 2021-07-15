def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b, c, d = Input()
    x, y = a + b, c + d
    
    if   x > y: print("Left")
    elif x < y: print("Right")
    else:       print("Balanced")


main()
