def prog(mass, st):
    nonlocal alf
    if st == st[0] * len(st):
        for i in range(26):
            if alf[i] == st[0]:
                mass[i] = (mass[i] + 1) * len(st) + mass[i]
            else:
                mass[i] = min(1, mass[i])
    else:
        mmm = razlog(st)
        r = 1
        while st[r] == st[r - 1]:
            r += 1
        k = 1
        while st[len(st) - k] == st[len(st) - k - 1]:
            k += 1
        for i in range(26):
            if alf[i] == st[0] and alf[i] == st[-1]:
                if mass[i] == 0:
                    mass[i] = max(mmm[i], k, r)
                else:
                    mass[i] = max(mmm[i], k + r + 1)
            elif alf[i] == st[0]:
                if mass[i] == 0:
                    mass[i] = max(mmm[i], r)
                else:
                    mass[i] = max(mmm[i], r + 1)
            elif alf[i] == st[-1]:
                if mass[i] == 0:
                    mass[i] = max(mmm[i], k)
                else:
                    mass[i] = max(mmm[i], k + 1)
            else:
                if mass[i] == 0:
                    mass[i] = mmm[i]
                else:
                    mass[i] = max(1, mmm[i])
    return mass


def razlog(st):
    nonlocal alf
    mass = [0 for i in range(26)]
    mass[alf.index(st[0])] = 1
    now = 1
    for i in range(1, len(st)):
        if st[i] == st[i - 1]:
            now += 1
        else:
            now = 1
        mass[alf.index(st[i])] = max(now, mass[alf.index(st[i])])
    return mass


n = int(input())
st = input()
alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mass = razlog(st)
for i in range(n - 1):
    sti = input()
    mass = prog(mass, sti)
print(max(mass))
