from itertools import combinations

N = int(input())
name_count = {'M': 0,
              'A': 0,
              'R': 0,
              'C': 0,
              'H': 0, }
for i in range(N):
    name = input()

    if name[0] in name_count:
        name_count[name[0]] += 1


def comb(n, r):
    up = 1
    down = 1
    for i in range(r):
        up *= n - i
        down *= i + 1
    return up // down


all_sum = sum(name_count.values())
total = comb(all_sum, 3)

for i in list(name_count.values()):
    if i >= 2:
        total -= comb(i, 2) * (all_sum - i)

    if i >= 3:
        total -= comb(i, 3)

print(total)
