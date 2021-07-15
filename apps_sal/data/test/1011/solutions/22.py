def lte(n, a, d):
    # count the number of values in a <= d
    if a[0] > d:
        return 0
    if a[-1] <= d:
        return n
    else:
        lo = 0
        hi = n - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if a[mid] <= d:
                lo = mid
            else:
                hi = mid
        return lo + 1

def score(n, m, a, b, d):
    ca = lte(n, a, d)
    cb = lte(m, b, d)

    a_score = 2 * ca + 3 * (n - ca)
    b_score = 2 * cb + 3 * (m - cb)

    return a_score, b_score


def main():
    n = int(input())
    a = list(map(int, input().split()))

    m = int(input())
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    factor = 2 if 2 * (n - m) > 3 * (n - m) else 3
    best_diff = factor * (n - m)
    best_a = factor * n
    out = str(factor * n) + ':' + str(factor * m)

    mega = set(a + b)

    for d in mega:
        if d <= 0: 
            continue

        a_score, b_score = score(n, m, a, b, d)
        diff = a_score - b_score

        if diff > best_diff or (diff == best_diff and a_score > best_a):
            best_diff = diff
            best_a = a_score
            out = str(a_score) + ':' + str(b_score)

    print(out)

main()

