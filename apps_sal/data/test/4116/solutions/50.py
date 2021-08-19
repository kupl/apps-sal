n = int(input())
b = 0
for a in range(9):
    if n / (a + 1) < 10 and n % (a + 1) == 0:
        b = 1
if b == 1:
    print('Yes')
else:
    print('No')
