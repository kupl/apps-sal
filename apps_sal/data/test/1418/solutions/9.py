def prost(i):
    for x in range(2, int(i ** 0.5 + 1)):
        if i % x == 0:
            return x
    return 1


l = 1
mass = []
for i in range(2, int(input()) + 1):
    if prost(i) == 1:
        mass.append(l)
        l += 1
    else:
        mass.append(mass[prost(i) - 2])
print(*mass)
