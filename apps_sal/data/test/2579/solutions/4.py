l, r, x, y, k = list(map(int, input().split()))


def f():
    for i in range(x, y + 1):
        n = i * k
        if l <= n <= r:
            print("YES")
            return
        if n > r:
            print("NO")
            return
    print("NO")
    return


f()
