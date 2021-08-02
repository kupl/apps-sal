from collections import defaultdict


def KKK():
    n = int(input())
    d = defaultdict(int)
    a = list(map(int, input().split()))
    se = set()
    for i in range(len(a)):
        d[a[i]] += 1
        se.add(a[i])

    s = 0
    while se:
        s += d[se.pop()] - 1

    minLen = 3000
    for i in range(len(a)):
        r = s
        newd = d.copy()
        for j in range(i, len(a)):
            if r == 0:
                minLen = min(j - i, minLen)
            if newd[a[j]] > 1:
                newd[a[j]] -= 1
                r -= 1
        if r == 0:
            minLen = min(len(a) - i, minLen)
    print(minLen)


KKK()
