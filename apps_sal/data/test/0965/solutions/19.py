n = int(input())
status = list(input())
allin = status.count('A')
folded = status.count('F')
In = status.count('I')
if In > 1:
    print(0)
if In == 1:
    print(1)
if In == 0:
    print(allin)
