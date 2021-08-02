ovmaxx = 0

t = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]

x = int(input())
y = list(map(int, input().split(' ')))

good = [False] * (10**5 + 5)
for i in y:
    good[i] = True


dp2 = [0] * (10**5 + 5)

for i in range(10**5 + 5):
    if not good[i]:
        continue
    pdiv = []

    for a in t:
        k = 0
        while i % a == 0:
            if k == 0:
                pdiv.append(a)
            i //= a
            k = 1
    maxx = 0
    if i != 1:
        pdiv.append(i)
    for i2 in pdiv:
        maxx = max(dp2[i2] + 1, maxx)

    for i2 in pdiv:
        dp2[i2] = max(dp2[i2] + 1, maxx)

    ovmaxx = max(ovmaxx, maxx)

print(max(ovmaxx, 1))
