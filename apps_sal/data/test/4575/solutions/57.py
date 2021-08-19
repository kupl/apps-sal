def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    n = int(input())
    (d, x) = Input()
    a = [int(input()) for _ in range(n)]
    ans = n
    for a_i in a:
        cnt = 1
        while True:
            flag = cnt * a_i + 1
            if flag > d:
                break
            ans += 1
            cnt += 1
    print(ans + x)


main()
