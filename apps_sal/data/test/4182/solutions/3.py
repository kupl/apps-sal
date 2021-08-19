def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (n, m, x, y) = Input()
    x_data = Input()
    y_data = Input()
    x_max = max(x_data)
    y_min = min(y_data)
    ans = False
    for i in range(-100, 101):
        if x_max < i <= y_min and x < i <= y:
            ans = True
            break
    if ans:
        print('No War')
    else:
        print('War')


main()
