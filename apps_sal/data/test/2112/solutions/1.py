__MULTITEST = False


def isSubseq(a, b):
    ptr = 0
    lenB = len(b)
    for x in a:
        if b[ptr] == x:
            ptr += 1
            if ptr == lenB:
                return True
    return False


def solve():
    (n, m) = map(int, input().split())
    (x, k, y) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if not isSubseq(a, b):
        print(-1)
    else:
        a.insert(0, -1)
        a.append(-2)
        b.insert(0, -1)
        b.append(-2)
        lenA = len(a)
        lenB = len(b)
        ans = 0
        pa1 = 0
        pa2 = 1
        pb = 0
        while pb + 1 < lenB:
            maxOfSeg = -3
            while a[pa1] != b[pb]:
                pa1 += 1
            pa2 = pa1 + 1
            while a[pa2] != b[pb + 1]:
                maxOfSeg = max(maxOfSeg, a[pa2])
                pa2 += 1
            segLen = pa2 - pa1 - 1
            if segLen >= k:
                if x > y * k:
                    if a[pa1] < maxOfSeg and a[pa2] < maxOfSeg:
                        ans += x + (segLen - k) * y
                    else:
                        ans += segLen * y
                else:
                    ans += segLen // k * x + segLen % k * y
            elif a[pa1] < maxOfSeg and a[pa2] < maxOfSeg:
                print(-1)
                return
            else:
                ans += segLen * y
            pb += 1
            pa1 = pa2
        print(ans)


def __starting_point():
    t = int(input()) if __MULTITEST else 1
    for tt in range(t):
        try:
            solve()
        except IndexError:
            print('-1')


__starting_point()
