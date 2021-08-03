n = int(input())
mass = list(map(int, input().split()))


def gcd(a, b):
    if b:
        return(gcd(b, a % b))
    else:
        return a


# def add(a, b):
    #k = 1
    # while gcd(k, a) != 1
# print(tmp_mass)
i = 0
c = len(mass)
count = 0
while i < c - 1:
    #print(i, c)
    k = gcd(mass[i], mass[i + 1])
    if k == 1:
        i += 1
        continue
    else:
        count += 1
        mass.insert(i + 1, 1)
        c += 1
        i += 2
print(count)
print(' '.join(map(str, mass)))
