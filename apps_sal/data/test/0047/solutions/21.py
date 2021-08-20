(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))


def factiry(arr, mul):
    (curMax, mulMax, gloMax, cur) = (0, 0, 0, 0)
    for i in range(n):
        curMax = max(arr[i] + curMax, 0)
        mulMax = max(mulMax + arr[i] * mul, curMax)
        cur = max(cur + arr[i], mulMax)
        gloMax = max(gloMax, cur)
    return gloMax


total = factiry(a, m)
print(total)
