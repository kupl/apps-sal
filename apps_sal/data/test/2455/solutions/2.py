# http://codeforces.com/contest/400/problem/0
# Codeforces : A. Inna and choose options

liste_a = (1, 2, 3, 4, 6, 12)
liste_results = []


def process(essai):
    nonlocal liste_results
    liste_av = [0]
    for a in liste_a:
        b = 12 // a
        for r in range(b):
            if essai[r::b] == 'X' * a:
                liste_av[0] += 1
                liste_av.append('{}x{}'.format(a, b))
                break
    liste_av[0] = str(liste_av[0])
    liste_results.append(liste_av)


t = int(input())
for k in range(t):
    essai = input()
    process(essai)

for s in liste_results:
    print(*s)
