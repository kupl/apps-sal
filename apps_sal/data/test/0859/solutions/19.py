from math import factorial
(s1, s2) = (input().strip(), input().strip())
(d, q) = (abs(s1.count('+') - s1.count('-') - s2.count('+') + s2.count('-')), s2.count('?'))
print(0 if d + q & 1 or d > q else factorial(q) / factorial(d + q >> 1) / factorial(q - d >> 1) / (1 << q))
