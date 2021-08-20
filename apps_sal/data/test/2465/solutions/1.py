def func(a, b):
    mini = min(a, b)
    maxi = max(a, b)
    while maxi % mini != 0:
        (maxi, mini) = (mini, maxi % mini)
    return (a // mini, b // mini)


def main():
    count = int(input())
    for x in range(count):
        ang = int(input())
        (a, b) = func(2 * ang, 360)
        if a > b - 2:
            print(b * 2)
        elif b == 1:
            print(3)
        elif b == 2:
            print(4)
        else:
            print(b)


main()
