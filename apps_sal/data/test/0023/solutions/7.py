a = list(map(int, input()))
b = list(map(int, input()))


if len(b) > len(a):
    a.sort(reverse=True)
    print(''.join(map(str, a)))
else:

    counts = [0] * 10
    for d in a:
        counts[d] += 1

    def rec(counts, i):
        if i >= len(b):
            return []

        d = b[i]
        if counts[d] > 0:
            counts[d] -= 1
            r = rec(counts, i + 1)
            if r is None:
                counts[d] += 1
            else:
                res = [d] + r
                return res

        for d in reversed(list(range(d))):
            if counts[d] > 0:
                counts[d] -= 1
                res = [d]
                for e in reversed(list(range(10))):
                    for _ in range(counts[e]):
                        res.append(e)
                return res

        return None

    print(''.join(map(str, rec(counts, 0))))
