n = int(input())
a1 = [int(v) for v in input().split()]
a2 = [int(v) for v in input().split()]
b = [int(v) for v in input().split()]


def make_prefixes(a):
    pref = [0, a[0]]
    for v in a[1:]:
        pref.append(pref[-1] + v)
    return pref


prefa1 = make_prefixes(a1)
prefa2 = make_prefixes(a2)
crosstimes = [prefa1[i] + b[i] + (prefa2[-1] - prefa2[i]) for i in range(n)]
crosstimes.sort()
print(crosstimes[0] + crosstimes[1])
