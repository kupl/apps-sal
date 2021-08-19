n = int(input())
a = 0
for i in range(n, 1, -1):
    if i % 2 == 1:
        a = a + 1
a = a + 1
print('{:.08f}'.format(a / n))
