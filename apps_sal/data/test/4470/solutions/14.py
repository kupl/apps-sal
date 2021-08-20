n = int(input())
for i in range(n):
    q = int(input())
    s = 0
    while q % 5 == 0:
        q = q // 5
        s += 3
    while q % 3 == 0:
        q = q // 3
        s += 2
    while q % 2 == 0:
        q = q // 2
        s += 1
    if q == 1:
        print(s)
    else:
        print(-1)
