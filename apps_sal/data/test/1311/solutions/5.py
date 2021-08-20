def read_data():
    n = int(input())
    ranges = []
    buffer = [input() for i in range(n)]
    for xw in buffer:
        (x, w) = map(int, xw.split())
        ranges.append((x + w, x - w))
    return (n, ranges)


def solve(n, ranges):
    ranges.sort()
    n = 0
    end = -float('inf')
    for (e, b) in ranges:
        if b >= end:
            n += 1
            end = e
    return n


(n, ranges) = read_data()
print(solve(n, ranges))
