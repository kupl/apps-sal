import math
n, k = [int(s) for s in input().split()]

a = [int(s) for s in input().split()]


def check():
    n = len(a)
    res = 0
    sum0 = 0
    for i in range(n):
        res0 = res
        if res == 0:
            if a[i] < k:
                res = a[i]
                if i == n - 1 and a[i] != 0:
                    sum0 += 1
            else:
                if i == n - 1:
                    sum0 += math.ceil((a[i]) / k)
                else:
                    sum0 += int((a[i]) / k)
                res = a[i] % k
        else:
            if i == n - 1:
                sum0 += math.ceil((a[i] + res) / k)
            else:
                sum0 += max(int((a[i] + res) / k), 1)
            res = (a[i] + res) % k if a[i] + res >= k else 0
    print(sum0)


check()
