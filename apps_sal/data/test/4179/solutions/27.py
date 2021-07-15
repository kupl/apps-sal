def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, m, c = Input()
    b = Input()
    a = [Input() for _ in range(n)]
    ans = 0
    for row in a:
        tmp = c
        for x, y in zip(row, b):
            tmp += x * y
        if tmp > 0:
            ans += 1
    print(ans)

main()
