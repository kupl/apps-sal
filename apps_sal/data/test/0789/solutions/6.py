d = set()


def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        midval = a[mid]
        if midval < x:
            lo = mid + 1
        elif midval > x:
            hi = mid
        else:
            return mid
    return -1


for i in range(512):
    s = str(bin(i))
    s = s[2:]
    s1 = ''
    s2 = ''
    for c in s:
        if(c == '0'):
            s1 += '4'
            s2 += '7'
        else:
            s1 += '7'
            s2 += '4'
    d.add(int(s1))
    d.add(int(s2))
l = list(d)
l.sort()

n = int(input())
print(binary_search(l, n) + 1)
