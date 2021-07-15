n = int(input())
a = 2
b = 3
c = 5
d = 7
print(n - n // a - n // b - n // c - n // d + n // (a * b) + n // (a * c) + n // (a * d) + n // (b * c) + n // (b * d) + n // (c * d) - n // (a * b * c) - n // (a * b * d) - n // (a * c * d) - n // (b * c * d) + n // (a * b * c * d))
