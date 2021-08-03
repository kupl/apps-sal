from collections import Counter
left_parts = Counter()
right_parts = Counter()
n = int(input())
for _ in range(n):
    seq = input()
    for res_counter, first_par, s in (left_parts, '(', seq), (right_parts, ')', reversed(seq)):
        res = 1
        for c in s:
            if c == first_par:
                res += 1
            elif res == 1:
                break
            else:
                res -= 1
        else:
            res_counter[res] += 1
res = 0
for key in list(left_parts.keys()):
    res += left_parts[key] * right_parts[key]
print(res)
