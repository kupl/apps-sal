a = input()


def a0o1(character):
    if character == 'r':
        return 0
    if character == 'b':
        return 1


def isPar(par):
    return par == 0


b = list(map(a0o1, input()))
par = 0
a1_miss_0 = 0
a1_miss_1 = 0
a2_miss_0 = 0
a2_miss_1 = 0
for x in b:
    a1_miss_0 += x == 0 and isPar(par)
    a1_miss_1 += x == 1 and (not isPar(par))
    a2_miss_0 += x == 0 and (not isPar(par))
    a2_miss_1 += x == 1 and isPar(par)
    par = (par + 1) % 2
a1_changes = abs(a1_miss_0 - a1_miss_1)
a1_swaps = max(a1_miss_0, a1_miss_1) - a1_changes
a_1 = a1_changes + a1_swaps
a2_changes = abs(a2_miss_0 - a2_miss_1)
a2_swaps = max(a2_miss_0, a2_miss_1) - a2_changes
a_2 = a2_changes + a2_swaps
print(min(a_1, a_2))
