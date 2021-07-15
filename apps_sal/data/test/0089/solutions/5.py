n = int(input())
if n % 2 == 0:
    b = 2
else:
    b = 1
s = 0
for i in range(b, n + 1, 2):
    s += i
print(s)
