n = int(input())


def s(n):
    k = 0
    for i in str(n):
        k += int(i)
    return k


while s(n) % 4 != 0:
    n += 1
print(n)
