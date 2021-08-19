n = int(input())
a = 0
b = 0
count = 0
while 3 ** a < n and count == 0:
    b = 0
    a += 1
    while 3 ** a + 5 ** b < n:
        b += 1
        if 3 ** a + 5 ** b == n:
            count = 1
if count == 1:
    print(a, b)
else:
    print(-1)
