from math import gcd
n = int(input())
arr = list(map(int, input().split()))


def getans():
    cnt1s = arr.count(1)
    if cnt1s > 0: return n - cnt1s
    minlen = n
    for i in range(n):
        g = arr[i]
        for j in range(i + 1, n):
            g = gcd(g, arr[j])
            if g == 1:
                minlen = min(minlen, j - i)
                break
    if minlen == n: return -1
    return (minlen + n - 1)


print(getans())
