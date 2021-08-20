"""Codeforces Round #555 (Div. 3)

Problem F. Maximum Balanced Circle

:author:         Kitchen Tong
:mail:    kctong529@gmail.com

Please feel free to contact me if you have any question
regarding the implementation below.
"""
__version__ = '0.1'
__date__ = '2019-04-26'
import sys


def solve(n, a):
    max_a = max(a)
    counter = [0 for i in range(max_a + 1)]
    for ai in a:
        counter[ai] += 1
    best_group = []
    best_total = 0
    curr = 1
    while curr <= max_a:
        if counter[curr] > 0:
            curr_group = [curr]
            curr_total = counter[curr]
            curr += 1
            if curr > max_a:
                break
            while counter[curr] > 1:
                curr_group.append(curr)
                curr_total += counter[curr]
                curr += 1
                if curr > max_a:
                    break
            if curr > max_a:
                break
            if counter[curr] > 0:
                curr_group.append(curr)
                curr_total += counter[curr]
            if curr_total > best_total:
                best_group = curr_group
                best_total = curr_total
        else:
            curr += 1
    if curr_total > best_total:
        best_group = curr_group
        best_total = curr_total
    seq = best_group
    for i in best_group[::-1]:
        seq += [i] * (counter[i] - 1)
    return (best_total, seq)


def main(argv=None):
    n = int(input())
    a = list(map(int, input().split()))
    (total, seq) = solve(n, a)
    print(total)
    print(' '.join(map(str, seq)))
    return 0


def __starting_point():
    STATUS = main()
    return STATUS


__starting_point()
