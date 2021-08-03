n = int(input())
sumn = 0
for a in range(1, n + 1):
    if n % a == 0:
        sumn += n // a - 1
    else:
        sumn += n // a
print(sumn)
