
n = int(input())


while True:
    z = list(str(n))
    z = list(map(int, z))
    if sum(z) % 4 == 0:
        break
    else:
        n += 1


print(n)
