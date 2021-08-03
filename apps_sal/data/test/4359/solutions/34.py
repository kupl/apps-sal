import math as m
A = []
min_digit = 9
for _ in range(5):
    s = input()
    n = int(s)
    digit = int(s[-1])
    if digit > 0 and digit < min_digit:
        min_digit = digit
        A = A + [n]
    else:
        A = [n] + A

A = [int(m.ceil(n / 10) * 10) for n in A[:-1]] + [A[-1]]
print(sum(A))
