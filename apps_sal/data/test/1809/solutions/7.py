from itertools import permutations as perm


def weigh(seq, order_seq):
    ret = 0
    w_seq = list(seq[:])
    for (idx, i) in enumerate(order_seq):
        for book_idx in w_seq[:w_seq.index(i)]:
            ret += weights[book_idx - 1]
        w_seq.insert(0, w_seq.pop(w_seq.index(i)))
    return ret


(n, m) = tuple(map(int, input().split(' ')))
weights = tuple(map(int, input().split(' ')))
order = tuple(map(int, input().split(' ')))
already = []
for i in order:
    if i not in already:
        already.append(i)
print(weigh(already, order))
