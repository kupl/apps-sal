def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    a = Input()
    b = Input()
    c = Input()
    ans = 0
    for i in range(n - 1):
        if a[i + 1] - a[i] == 1:
            ans += c[a[i] - 1]
    ans += sum(b)
    print(ans)


main()
