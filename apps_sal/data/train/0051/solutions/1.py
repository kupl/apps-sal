import itertools
import sys


'''
w1 - w2 = d1
w2 - w3 = d2
w1 + w2 + w3 = k

w1 = w2 + d1
w3 = w2 - d2
w2 + d1 + w2 + w2 - d2 = k

w2 = (k - d1 + d2) / 3
w1 = w2 + d1
w3 = w2 - d2
'''
for _ in range(int(input())):

    n, k, d1, d2 = list(map(int, str.split(sys.stdin.readline())))
    for s1, s2 in itertools.product((1, -1), repeat=2):

        cd1, cd2 = d1 * s1, d2 * s2
        w2 = k - cd1 + cd2
        if w2 % 3 != 0:

            continue

        w2 //= 3
        w1 = w2 + cd1
        w3 = w2 - cd2
        if w1 >= 0 and w2 >= 0 and w3 >= 0:

            d = n - k
            mw = max((w1, w2, w3))
            nw = 3 * mw - w1 - w2 - w3
            if d >= nw and (d - nw) % 3 == 0:

                print("yes")
                break

    else:

        print("no")
