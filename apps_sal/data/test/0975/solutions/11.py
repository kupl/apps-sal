from collections import Counter

n = int(input())

a = [int(x) for x in input()]
b = [int(x) for x in input()]

a.sort(reverse=True)
b.sort(reverse=True)

cur_b = 0
for a_i in a:
    if b[cur_b] > a_i:
        cur_b += 1

punches = 0
cur_b2 = 0
for a_i in a:
    if b[cur_b2] >= a_i:
        cur_b2 += 1
    else:
        punches += 1

print(punches)
print(cur_b)

