N = int(input())

A = list(map(int, input().split()))

A.sort()

s1 = 0
s2 = 0

at = -1
atc = 0

for a in A:
    if at == a:
        atc += 1

    else:
        if atc >= 4:
            s1 = at
            s2 = at
        elif atc >= 2:
            s2 = s1
            s1 = at

        at = a
        atc = 1

if atc >= 4:
    s1 = at
    s2 = at
elif atc >= 2:
    s2 = s1
    s1 = at

print((s1 * s2))
