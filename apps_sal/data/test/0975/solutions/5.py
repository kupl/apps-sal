n = int(input())
a = sorted(map(int, input()))
b = sorted(map(int, input()))

r1 = n
j = 0
try:
    for i in range(n):
        while a[i] > b[j]:
            j += 1
            if j >= n:
                raise UserWarning
        r1 -= 1
        j += 1
        if j >= n:
            raise UserWarning
except UserWarning:
    pass

r2 = 0
j = 0
try:
    for i in range(n):
        while a[i] >= b[j]:
            j += 1
            if j >= n:
                raise UserWarning
        r2 += 1
        j += 1
        if j >= n:
            raise UserWarning
except UserWarning:
    pass

print(r1)
print(r2)

