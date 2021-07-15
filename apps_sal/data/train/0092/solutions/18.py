n = int(input())
for i in range(n):
    m1 = set(list(input()))
    m2 = set(list(input()))
    f = 'NO'
    for el in m1:
        if el in m2:
            f = 'YES'
    print(f)
