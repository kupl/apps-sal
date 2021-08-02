from pprint import pprint
from operator import itemgetter


def main():
    _ = int(input().strip())
    w1 = input().strip()
    w2 = input().strip()

    if len(w1) != len(w2):
        return -1

    hdis, fpos, lpos = one_replace_hamming(w1, w2)
    print(hdis)
    print(min(fpos + 1, lpos + 1), max(fpos + 1, lpos + 1))


def ham_wt(w1, w2):
    diff_pairs1 = []
    rev_assoc = dict()
    pos_indicator = dict()
    for i in range(len(w1)):
        if w2[i] != w1[i]:
            diff_pairs1.append((w1[i], w2[i]))
            rev_assoc[w2[i]] = w1[i]
            pos_indicator[w1[i], w2[i]] = i
    return (diff_pairs1, rev_assoc, pos_indicator)


def one_replace_hamming(w1, w2):
    diff_pairs, rev_assoc, pos_indicator = ham_wt(w1, w2)

    for fst, snd in diff_pairs:
        if fst in rev_assoc and rev_assoc[fst] == snd:
            return (len(diff_pairs) - 2, pos_indicator[fst, snd], pos_indicator[snd, fst])

    for fst, snd in diff_pairs:
        if fst in rev_assoc:
            return (len(diff_pairs) - 1, pos_indicator[fst, snd], pos_indicator[rev_assoc[fst], fst])

    return (len(diff_pairs), -2, -2)


def __starting_point():
    main()


__starting_point()
