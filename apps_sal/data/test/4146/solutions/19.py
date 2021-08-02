from collections import Counter

n = int(input())
v = list(map(int, input().split()))

even = v[::2]
odd = v[1::2]

c_even = Counter(even)
c_odd = Counter(odd)

e_max1 = [0, 0]
e_max2 = [0, 0]
o_max1 = [0, 0]
o_max2 = [0, 0]

for x, y in list(c_even.items()):
    if y > e_max1[1]:
        e_max2 = e_max1
        e_max1 = [x, y]
    elif y > e_max2[1]:
        e_max2 = [x, y]

for x, y in list(c_odd.items()):
    if y > o_max1[1]:
        o_max2 = o_max1
        o_max1 = [x, y]
    elif y > o_max2[1]:
        o_max2 = [x, y]


if e_max1[0] == o_max1[0]:
    print((min(n - e_max1[1] - o_max2[1], n - e_max2[1] - o_max1[1])))
else:
    print((n - e_max1[1] - o_max1[1]))
