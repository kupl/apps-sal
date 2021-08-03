n, x = list(map(int, input().split()))

a, b = [1], [1]

for i in range(n):
    a.append(a[i] * 2 + 3)
    b.append(b[i] * 2 + 1)


def cal(n, x):
    if n == 0:
        if x <= 0:
            return 0
        else:
            return 1
    val = (a[n] + 1) // 2

    if x < val:
        return cal(n - 1, x - 1)
    elif x == val:
        return b[n - 1] + 1
    elif x > val:
        return b[n - 1] + 1 + cal(n - 1, x - val)


ans = cal(n, x)
print(ans)
