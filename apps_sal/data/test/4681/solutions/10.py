n = int(input())
(a, b) = (2, 1)
for i in range(n):
    (a, b) = (b, a + b)
print(a)
