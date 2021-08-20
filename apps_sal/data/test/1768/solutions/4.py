import string
import bisect
import sys


def main():
    lines = sys.stdin.readlines()
    n = int(lines[0])
    s = lines[1]
    vals = {}
    for c in string.ascii_lowercase:
        a = [i for (i, ch) in enumerate(s) if ch == c]
        m = len(a)
        b = [0]
        for length in range(1, m + 1):
            best = n
            for i in range(m - length + 1):
                j = i + length - 1
                best = min(best, a[j] - j - (a[i] - i))
            b.append(best)
        vals[c] = b
    q = int(lines[2])
    r = []
    idx = 3
    while q > 0:
        q -= 1
        query = lines[idx].split()
        idx += 1
        m = int(query[0])
        c = query[1]
        i = bisect.bisect_right(vals[c], m)
        r.append(str(min(n, i + m - 1)))
    print('\n'.join(r))


main()
