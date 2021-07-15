from itertools import permutations as p


def razn(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def sp(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def su(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

a = list(tuple(map(int, input().split())) for i in range(8))
cp = sorted(sorted(el) for el in a)
for p1 in p(a[0]):
    for i in range(1, 8):
        for j in range(i + 1, 8):
            for l in range(j + 1, 8):
                for p2 in p(a[i]):
                    for p3 in p(a[j]):
                        for p4 in p(a[l]):
                            s2 = razn(p2, p1)
                            s3 = razn(p3, p1)
                            s4 = razn(p4, p1)
                            le = sp(s2, s2)
                            if le and sp(s3, s3) == le and sp(s4, s4) == le and sp(s2, s3) == 0 and sp(s2, s4) == 0 and sp(s3, s4) == 0:
                                mass = [su(su(s3, s4), p1), su(su(s3, s2), p1), su(su(s2, s4), p1), p1, p2, p3, p4, su(su(su(s3, s4), p1), s2)]
                                if sorted(sorted(el) for el in mass) == cp:
                                    print("YES")
                                    for el in a:
                                        tmp = sorted(el)
                                        for kk in range(8):
                                            if sorted(mass[kk]) == tmp:
                                                print(mass[kk][0], mass[kk][1], mass[kk][2])
                                                mass[kk] = ()
                                                break
                                    return
print("NO")
