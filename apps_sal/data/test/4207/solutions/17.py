from fractions import Fraction
n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
extra_count = 0
counts_map = dict()
for (ai, bi) in zip(a, b):
    if ai != 0:
        fi = Fraction(-1 * bi, ai)
        num_i = fi.numerator
        den_i = fi.denominator
        curr_str = str(num_i) + '#' + str(den_i)
        if curr_str in counts_map:
            counts_map[curr_str] += 1
        else:
            counts_map[curr_str] = 1
    elif bi == 0:
        extra_count += 1
    else:
        pass
max = 0
for key in counts_map:
    curr_count = counts_map[key]
    if curr_count > max:
        max = curr_count
print(max + extra_count)
