# Python Template

from sys import stdin, stdout
from math import ceil


def main():
    t = 1
    for _ in range(t):
        n = int(stdin.readline())
        a = [int(i) for i in stdin.readline().split()]
        q = int(stdin.readline())
        diffs = [0] * (n - 1)
        start = a[0]
        for i in range(n - 1):
            diffs[i] = a[i + 1] - a[i]

        upstep = 0
        for d in diffs:
            if d > 0:
                upstep += d
        val = ceil((start + upstep) / 2.0)
        # print(diffs)
        print(val)
        # print()

        for _ in range(q):
            l, r, x = [int(i) for i in stdin.readline().split()]
            l -= 1
            r -= 1
            if l == 0:
                start += x
            else:
                old = diffs[l - 1]
                diffs[l - 1] += x
                new = diffs[l - 1]
                if old > 0:
                    upstep -= old
                if new > 0:
                    upstep += new
            if r != n - 1:
                old = diffs[r]
                diffs[r] -= x
                new = diffs[r]
                if old > 0:
                    upstep -= old
                if new > 0:
                    upstep += new
            #print("Steps: {0}".format(upstep))
            # print(diffs)
            #print("Start: {0}".format(start))

            val = ceil((start + upstep) / 2.0)
            #print("Answer: {0}".format(val))
            print(val)


main()
