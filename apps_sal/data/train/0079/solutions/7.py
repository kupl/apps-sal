from sys import stdin
input = stdin.readline
q = int(input())
for _ in range(q):
    n = int(input())
    pier = []
    i = 2
    nn = n
    while True:
        if nn % i == 0:
            pier.append(i)
            nn //= i
        else:
            i += 1
        if i ** 2 > n:
            break
    if nn != 1:
        pier.append(nn)
    pier_unique = list(set(pier))
    dzielniki = [1]
    for p in pier_unique:
        pot = p
        addition = []
        while n % pot == 0:
            addition1 = [d * pot for d in dzielniki]
            addition += addition1
            pot *= p
        dzielniki += addition
    dzielniki = dzielniki[1:]
    k = len(pier_unique)
    if k == 1:
        print(*dzielniki)
        print(0)
    elif k >= 3:
        dzielniki = set(dzielniki)
        odp = []
        for i in range(k):
            dzielniki.remove(pier_unique[i - 1] * pier_unique[i])
        for i in range(k):
            odp.append(pier_unique[i - 1] * pier_unique[i])
            to_rem = []
            for dz in dzielniki:
                if dz % pier_unique[i] == 0:
                    to_rem.append(dz)
                    odp.append(dz)
            for to in to_rem:
                dzielniki.remove(to)
        print(*odp)
        print(0)
    else:
        p = pier_unique[0]
        q = pier_unique[1]
        if n == p * q:
            print(p, q, p * q)
            print(1)
        else:
            test = p ** 2
            if n % test != 0:
                (p, q) = (q, p)
            dzielniki = set(dzielniki)
            dzielniki.remove(p * q)
            dzielniki.remove(p * p * q)
            odp = [p * q]
            to_rem = []
            for dzu in dzielniki:
                if dzu % p == 0:
                    to_rem.append(dzu)
                    odp.append(dzu)
            for tu in to_rem:
                dzielniki.remove(tu)
            odp.append(p * p * q)
            for dzu in dzielniki:
                odp.append(dzu)
            print(*odp)
            print(0)
