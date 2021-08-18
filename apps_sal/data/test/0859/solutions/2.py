
import itertools


s1 = input()
s2 = input()

s1_p = s1.count('+')
s1_n = s1.count('-')

s2_p = s2.count('+')
s2_n = s2.count('-')
s2_q = s2.count('?')

correct_pos = s1_p - s1_n
drea_pos = s2_p - s2_n

diff_pos = correct_pos - drea_pos

if s2_q == 0:
    if diff_pos == 0:
        print(1.0)
    else:
        print(0.0)
else:
    num = 0
    den = 0
    for c in itertools.product([1, -1], repeat=s2_q):
        if sum(c) == diff_pos:
            num += 1
        den += 1
    print("{0:.10f}".format(float(num) / den))
