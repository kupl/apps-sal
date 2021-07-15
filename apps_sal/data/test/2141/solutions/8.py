n = int(input())
a = 'WB' * (n // 2)
b = 'BW' * (n // 2)
if n & 1:
    a += 'W'
    b += 'B'
for i in range(n):
    print(a if i & 1 else b)
