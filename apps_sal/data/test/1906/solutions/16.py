n = int(input())
a = n // 2 + n // 3 + n // 5 + n // 7
b = n // 6 + n // 10 + n // 14 + n // 15 + n // 21 + n // 35
c = n // 30 + n // 42 + n // 70 + n // 105
d = n // 210
print(n - (a - b + c - d))
