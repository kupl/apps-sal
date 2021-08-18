N = int(input())
a = 1
b = 0
while 5**b < N:
    b += 1
if b <= 0:
    print((-1))
    return

while 3 ** a <= N:
    while b > 1 and 3**a + 5**b > N:
        b -= 1
    if 3**a + 5**b == N:
        print((str(a) + ' ' + str(b)))
        return
    else:
        a += 1
print((-1))
