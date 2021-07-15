lst = [0, 0, 4, 8]
mod = 10 ** 9 + 7
for i in range(4, 10 ** 6 + 1):
    lst.append((lst[-1] * 2) % mod)


def main(case):
    r, g, b, w = list(map(int, input().split()))
    if (r % 2) + (g % 2) + (b % 2) + (w % 2) <= 1:
        print("Yes")
    else:

        d = min(r, g, b, 1)
        w += d * 3
        r -= d
        g -= d
        b -= d
        if (r % 2) + (g % 2) + (b % 2) + (w % 2) <= 1:
            print("Yes")
        else:
            print("No")


def __starting_point():
    t = int(input())
    for i in range(t):
        main(i + 1)

__starting_point()
