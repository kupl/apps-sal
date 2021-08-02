def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, t = Input()
    data = [Input() for _ in range(n)]
    ans = 1001

    for cost, time in data:
        if time <= t:
            ans = min(ans, cost)

    if ans == 1001:
        print("TLE")
    else:
        print(ans)


main()
