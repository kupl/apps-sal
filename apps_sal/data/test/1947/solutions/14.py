import sys


def count_it():
    return len(''.join(list([' ' if x <= l else '1' for x in h])).split())


n, m, l = list([int(x) for x in sys.stdin.readline().split(' ')])
h = list([int(x) for x in sys.stdin.readline().split(' ')])
k = count_it()
for mi in range(m):
    request = sys.stdin.readline().split(' ')
    if len(request) == 1:
        print(k)
    else:
        r, p, d = list([int(x) for x in request])
        h[p - 1] += d
        if (h[p - 1] > l) and (h[p - 1] - d <= l):
            if n == 1:
                k += 1
            else:
                if (p - 1 == 0 and h[1] <= l) or (p == len(h) and h[p - 2] <= l) or (h[p - 2] <= l and h[p] <= l):
                    k += 1
                elif p - 1 != 0 and p != len(h) and h[p - 2] > l and h[p] > l:
                    k -= 1
