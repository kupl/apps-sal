import bisect

n, m, k, q = map(int, input().split())

# min, max
vals = {}
vals[1] = [1, 1]
for i in range(k):
    r, c = map(int, input().split())
    if r not in vals:
        vals[r] = [c, c]
    else:
        vals[r][0] = min(vals[r][0], c)
        vals[r][1] = max(vals[r][1], c)

q = list(map(int, input().split()))
q.sort()


def find_shortest(lower, upper, row):
    if row == 1:
        return upper - 1

    if lower > upper:
        return find_shortest(upper, lower, row)

    pos = bisect.bisect_left(q, lower)
    options = []
    if pos < len(q):
        if q[pos] <= upper:
            return upper - lower
        else:
            options.append(q[pos] - lower + q[pos] - upper)

    pos2 = bisect.bisect_left(q, lower) - 1
    if pos2 >= 0:
        options.append(lower - q[pos2] + upper - q[pos2])
    return min(options)


highest = 1
old_a, old_b = 0, 0
pos_a, pos_b = 1, 1
for row in range(1, n + 1):
    if not row in vals:
        continue
    highest = row
    row_min, row_max = vals[row]

    new_a = min(old_a + find_shortest(pos_a, row_max, row), old_b + find_shortest(pos_b, row_max, row)) + row_max - row_min
    new_b = min(old_a + find_shortest(pos_a, row_min, row), old_b + find_shortest(pos_b, row_min, row)) + row_max - row_min

    old_a, old_b = new_a, new_b
    pos_a, pos_b = row_min, row_max
    #print(old_a, old_b)

total = highest - 1
total += min(old_a, old_b)

print(total)
