n = int(input())
l = list(map(int, input().split()))


def sgn(x):
    if x > 0:
        return 1
    else:
        return -1


s = sgn(l[0])
wynik = 0
zera = 0
for i in range(n):
    wynik += abs(l[i]) - 1 if l[i] != 0 else 1
    if l[i] == 0:
        zera = 1
if zera == 1:
    print(wynik)
else:
    mn = 1
    for i in range(n):
        mn *= sgn(l[i])
    if mn == 1:
        print(wynik)
    else:
        print(wynik + 2)
