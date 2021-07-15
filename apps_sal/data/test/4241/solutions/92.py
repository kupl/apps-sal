def compare_s(s1, s2):
    ret = 0
    for i1, i2 in zip(s1, s2):
        if i1 != i2:
            ret += 1
    return ret


s = input()
t = input()
min_ = 1001

for i in range(len(s) - len(t) + 1):
    temp = compare_s(t, s[i:])
    if temp < min_:
        min_ = temp

print(min_)
