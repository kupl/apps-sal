def mergesort(s):
    if len(s) == 1:
        return s
    s1 = mergesort(s[:len(s) // 2])
    s2 = mergesort(s[len(s) // 2:])
    return merge(s1, s2)


def merge(s1, s2):
    f = []
    ind1 = 0
    ind2 = 0
    while ind1 != len(s1) and ind2 != len(s2):
        if str(s1[ind1]) + str(s2[ind2]) > str(s2[ind2]) + str(s1[ind1]):
            f.append(s2[ind2])
            ind2 += 1
        else:
            f.append(s1[ind1])
            ind1 += 1
    if ind1 != len(s1):
        f.extend(s1[ind1:])
    else:
        f.extend(s2[ind2:])
    return f


n = int(input())
s = []
for i in range(n):
    s.append(input())
print(''.join(mergesort(s)))
