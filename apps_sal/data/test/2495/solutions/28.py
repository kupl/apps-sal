n = int(input())
a = list(map(int, input().split()))
ans1 = abs(a[0] - 1)
ans2 = abs(a[0] + 1)
ans3 = 0


def f(x, y):
    for i in range(1, n):
        if y > 0:
            y += a[i]
            if y < 0:
                continue
            else:
                x += abs(y + 1)
                y = -1
        else:
            y += a[i]
            if y > 0:
                continue
            else:
                x += abs(y - 1)
                y = 1
    return x


if a[0] == 0:
    ans3 = float("inf")
else:
    ans3 = f(ans3, a[0])
print(min(ans3, f(ans1, 1), f(ans2, -1)))
