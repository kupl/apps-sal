from math import sqrt
import sys
input = sys.stdin.readline
n = int(input())
(a, b) = map(int, input().split())
diva = set()
divb = set()
for i in range(2, int(sqrt(a)) + 1):
    if a % i == 0:
        while a % i == 0:
            a //= i
        diva.add(i)
if a > 1:
    diva.add(a)
for i in range(2, int(sqrt(b)) + 1):
    if b % i == 0:
        while b % i == 0:
            b //= i
        divb.add(i)
if b > 1:
    divb.add(b)
alldiv = diva | divb
for _ in range(n - 1):
    (e, q) = map(int, input().split())
    trash = []
    for k in alldiv:
        if e % k != 0 and q % k != 0:
            trash.append(k)
    for k in trash:
        alldiv.remove(k)
res = list(alldiv)
if len(res) == 0:
    print(-1)
else:
    print(res[0])
