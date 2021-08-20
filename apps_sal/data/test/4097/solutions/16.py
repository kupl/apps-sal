def solve(seq):
    if len(seq) <= 2:
        return 0
    startings = []
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            start = (seq[1] + y, seq[0] + x - seq[1] - y, int(x != 0) + int(y != 0))
            startings.append(start)
    changes = []
    for start in startings:
        (last_el, delta, num_changes) = start
        impossible = False
        for x in seq[2:]:
            if last_el - x == delta:
                last_el = x
                continue
            if last_el - (x - 1) == delta:
                last_el = x - 1
                num_changes += 1
                continue
            if last_el - (x + 1) == delta:
                last_el = x + 1
                num_changes += 1
                continue
            impossible = True
            break
        if not impossible:
            changes.append(num_changes)
    return min(changes or [-1])


if '__main__' == __name__:
    input()
    print(solve(list(map(int, input().strip().split()))))
