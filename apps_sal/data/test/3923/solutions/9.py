ans = []


def go(base, n):
    ans.append(base + n - 1)
    for i in range(base, base + n - 1):
        ans.append(i)


def solve(n, a, b, x):
    cur_start = 1
    y = (n - a * x) // b

    for i in range(x):
        go(cur_start, a)
        cur_start += a

    for i in range(y):
        go(cur_start, b)
        cur_start += b


n, a, b = list(map(int, input().split()))


for x in range(0, 10 ** 6 + 1):
    if (n - x * a) % b == 0 and n - x * a >= 0:
        solve(n, a, b, x)
        print(' '.join(map(str, ans)))
        break
else:
    print(-1)


# Made By Mostafa_Khaled
