n, bx = list(map(int, input().split()))

num = list(map(int, input().split()))

num.reverse()

orig = 0
for i in range(0, len(num)):
    orig += num[i] * bx**i


n, bx2 = list(map(int, input().split()))

num = list(map(int, input().split()))

num.reverse()

orig2 = 0
for i in range(0, len(num)):
    orig2 += num[i] * bx2**i


if orig == orig2:
    print('=')
elif orig < orig2:
    print('<')
else:
    print('>')
