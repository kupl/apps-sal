from sys import stdin
input = stdin.readline
n = int(input())
l = list(map(int, input().split()))
ile = [0] * 21
for i in l:
    ind = 0
    while i > 0:
        if i % 2 == 1:
            ile[ind] += 1
        ind += 1
        i //= 2
pot = [1] * 22
for i in range(1, 22):
    pot[i] = pot[i - 1] * 2
wyn = 0
for j in range(n):
    liczba = 0
    for i in range(21):
        if ile[i] > 0:
            liczba += pot[i]
            ile[i] -= 1
    wyn += liczba ** 2
print(wyn)
