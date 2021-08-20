(n, m) = list(map(int, input().split()))
an = list(map(int, input().split()))
avtobus = 0
m2 = m
for grupp in an:
    if m2 >= grupp:
        m2 -= grupp
    else:
        m2 = m - grupp
        avtobus += 1
print(avtobus + 1)
