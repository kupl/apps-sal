from collections import Counter


def readints():
    return [int(item) for item in input().strip().split()]


class Solver:

    def main(self):
        n = readints()[0]
        a = readints()
        c = Counter(a)
        skipped = set()
        to_be_added = sorted(set(range(1, n + 1)) - set(c.keys()))
        changes = 0
        for i in range(n):
            if c[a[i]] > 1:
                if a[i] < to_be_added[changes] and a[i] not in skipped:
                    skipped.add(a[i])
                else:
                    c[a[i]] -= 1
                    a[i] = to_be_added[changes]
                    changes += 1
        print(changes)
        print(' '.join(map(str, a)))


Solver().main()
