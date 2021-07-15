import math
line = input().split()
a = int(line[0])
b = int(line[1])
if a == 0 and b == 0:
    print("infinity")
elif a == 0:
    print("0")
elif a== b:
    print("infinity")
elif a < b:
    print("0")
else:
    c = a- b;
    out = 0
    cek = [1]
    dum = c
    if dum % 2 == 0:
        cek.append(2)
        while dum % 2 == 0:
            dum /= 2
            for i in range(len(cek)):
                cek.append(cek[i] * 2)
    cek = list(set(cek))
    border = int(math.sqrt(dum))
    for i in range(3,border+1,2):
        if dum % i == 0:
            cek.append(i)
            while dum % i == 0:
                dum /= i
                for j in range(len(cek)):
                    cek.append(cek[j] * i)
    dum = int(dum)
    if dum != 0:
        for j in range(len(cek)):
            cek.append(cek[j] * dum)
    cek = list(set(cek))
    cek.sort()
    for i in cek:
        if i == 0:
            continue
        if c % i == 0:
            result = c / i
            if result <= b:
                break
            out += 1
    print(out)

