
url = "https://atcoder.jp//contests/abc047/tasks/abc047_b"

def main():
    w, h, n = list(map(int, input().split()))
    xya = [list(map(int, input().split())) for _ in range(n)]
    x, y = [0, w], [0, h]
    for low in xya:
        if low[2] == 1 and x[0] < low[0]:
            x[0] = low[0]
        elif low[2] == 2 and x[1] > low[0]:
            x[1] = low[0]
        elif low[2] == 3 and y[0] < low[1]:
            y[0] = low[1]
        elif low[2] == 4 and y[1] > low[1]:
            y[1] = low[1]
    xs = x[1] - x[0]
    ys = y[1] - y[0]
    if xs < 0 or ys < 0:
        print((0))
    else:
        ans = xs * ys
        print(ans)



def __starting_point():
    main()

__starting_point()
