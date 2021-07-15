def check(n2, n3, k):
    q2 = k // 2
    q3 = k // 3
    q6 = k // 6
    q2 -= q6
    q3 -= q6
    lo = n2 - q2
    hi = q3 + q6 - n3
    return lo <= hi and lo <= q6 and 0 <= hi

def go(n2, n3):
    lo = -1
    hi = int(6e7)
    while lo + 1 < hi:
        k = (lo + hi) // 2
        if check(n2, n3, k):
            hi = k
        else:
            lo = k
    return hi

n2, n3 = list(map(int, input().split()))
print(go(n2, n3))

