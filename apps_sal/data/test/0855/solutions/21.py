def readints():
    return [int(item) for item in input().strip().split()]


def cmp(a, b):
    return {
        1: {1: (0, 0), 2: (0, 1), 3: (1, 0)},
        2: {1: (1, 0), 2: (0, 0), 3: (0, 1)},
        3: {1: (0, 1), 2: (1, 0), 3: (0, 0)}
    }[a][b]


class Solver:
    def main(self):
        n, a, b = readints()
        A = [0, [0] + readints(), [0] + readints(), [0] + readints()]
        B = [0, [0] + readints(), [0] + readints(), [0] + readints()]

        current = (a, b)
        results = [current]

        while True:
            current = (A[current[0]][current[1]], B[current[0]][current[1]])
            if current not in results:
                results.append(current)
            else:
                break

        first_cycle = results.index(current)
        totals = 0, 0
        for i in range(first_cycle):
            res = cmp(*results[i])
            totals = totals[0] + res[0], totals[1] + res[1]
            n -= 1
            if n == 0:
                break

        cycled = len(results) - first_cycle
        if n > 0:
            multi = n // cycled
            for i in range(first_cycle, len(results)):
                res = cmp(*results[i])
                totals = totals[0] + multi * res[0], totals[1] + multi * res[1]

            for i in range(n % cycled):
                res = cmp(*results[i + first_cycle])
                totals = totals[0] + res[0], totals[1] + res[1]

        print('{} {}'.format(*totals))


Solver().main()

