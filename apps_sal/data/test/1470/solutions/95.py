X = int(input())
t = X // (6 + 5)
a = X % (6 + 5)
b = 0
if a > 6:
    b = 2
elif a == 0:
    b = 0
else:
    b = 1
print(2 * t + b)
