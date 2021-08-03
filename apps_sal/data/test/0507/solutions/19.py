size = int(input())
a = [int(elem) for elem in input().split()]
b = [int(elem) for elem in input().split()]

right = []
a_remain = []
b_remain = []
cand = []
for idx in range(size):
    if a[idx] == b[idx]:
        right.append(a[idx])
    else:
        right.append(0)
        a_remain.append(a[idx])
        b_remain.append(b[idx])

for elem in range(1, size + 1):
    if elem not in right:
        cand.append(elem)


def diff(seq_a, seq_b):
    if (seq_a[0] == seq_b[0] and seq_a[1] != seq_b[1]) or \
       (seq_a[0] != seq_b[0] and seq_a[1] == seq_b[1]):
        return True
    else:
        return False


def replace(original, pattern):
    pos = 0
    for idx, elem in enumerate(original):
        if elem == 0:
            original[idx] = pattern[pos]
            pos += 1
    return [str(elem) for elem in original]


if len(cand) == 1:
    print(' '.join(replace(right, cand)))
elif diff(cand, a_remain) and diff(cand, b_remain):
    print(' '.join(replace(right, cand)))
else:
    cand.reverse()
    print(' '.join(replace(right, cand)))
