from math import gcd

def make_kazu_list(n):
    l = [0]*n
    l[1] = 1
    i = 2
    while i < n:
        if l[i] == 0:
            j = i
            while j < n:
                l[j] = i if l[j] == 0 else l[j]
                j += i
        i += 1
    return l

def soinsuubunkai(n, l):
    r = []
    if n < 2:
        return r
    while l[n] != n:
        r.append(l[n])
        n = n // l[n]
    r.append(l[n])
    return set(r)

# l = make_kazu_list(101)
# print(soinsuubunkai(2, l))
# print(soinsuubunkai(66, l))
# print(soinsuubunkai(72, l))

def f(n, ais):
    pl = [False]*1000001
    l = make_kazu_list(1000001)
    for n in soinsuubunkai(ais[0], l):
        pl[n] = True
    common_factors = ais[0]
    pairwise_coprime = True
    setwise_coprime = False
    for ai in ais[1:]:
        if not pairwise_coprime and setwise_coprime:
            break
        if pairwise_coprime:
            numbers = soinsuubunkai(ai, l)
            for n in numbers:
                if pl[n]:
                    pairwise_coprime = False
                    break
                else:
                    pl[n] = True
        if not setwise_coprime:
            common_factors = gcd(common_factors, ai)
            if common_factors == 1:
                setwise_coprime = True
    if pairwise_coprime:
        return 'pairwise coprime'
    elif setwise_coprime:
        return 'setwise coprime'
    else:
        return 'not coprime'

n = int(input())
ais = list(map(int, input().split(' ')))
print((f(n, ais)))

