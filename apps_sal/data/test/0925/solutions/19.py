n = int(input())
y = n % 10
d = n // 10
if y == 0:
    a = [0, 8]
if y == 1:
    a = [0, 1, 3, 4, 7, 8, 9]
if y == 2:
    a = [2, 8]
if y == 3:
    a = [3, 8, 9]
if y == 4:
    a = [4, 8, 9]
if y == 5:
    a = [5, 6, 8, 9]
if y == 6:
    a = [6, 8]
if y == 7:
    a = [0, 3, 7, 8, 9]
if y == 8:
    a = [8]
if y == 9:
    a = [8, 9]
if d == 0:
    b = [0, 8]
if d == 1:
    b = [0, 1, 3, 4, 7, 8, 9]
if d == 2:
    b = [2, 8]
if d == 3:
    b = [3, 8, 9]
if d == 4:
    b = [4, 8, 9]
if d == 5:
    b = [5, 6, 8, 9]
if d == 6:
    b = [6, 8]
if d == 7:
    b = [0, 3, 7, 8, 9]
if d == 8:
    b = [8]
if d == 9:
    b = [8, 9]
print(len(a) * len(b))
