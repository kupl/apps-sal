n, a = list(map(int, input().split()))
x = list(map(int, input().split()))

x.sort()
res = 2**30


def solve(a, i, j):
    if a >= x[j]:
        return a - x[i]
    elif a <= x[i]:
        return x[j] - a
    else:
        sumLeft = (a - x[i]) * 2 + x[j] - a
        sumRight = (x[j] - a) * 2 + a - x[i]
        return min(sumLeft, sumRight)


if n <= 1:
    res = 0

elif n == 2:
    for value in x:
        res = min(res, abs(value - a))
else:
    if a <= x[0]:
        res = x[len(x) - 2] - a
    elif a >= x[len(x) - 1]:
        res = a - x[1]
    else:
        leftValue = solve(a, 1, len(x) - 1)
        rightValue = solve(a, 0, len(x) - 2)
        res = min(leftValue, rightValue)

print(res)
