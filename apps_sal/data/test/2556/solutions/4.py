n = int(input())
for i in range(n):
    (c, s) = tuple(map(int, input().split()))
    standart = s // c
    ost = s % c
    print((standart + 1) ** 2 * ost + standart ** 2 * (c - ost))
