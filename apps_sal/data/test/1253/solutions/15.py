a, b = list(map(int, input().split()))
x = list(map(int, input().split()))
x.sort()

for i in range(a):
    if x[i] < 0:
        x[i] *= -1
        b -= 1
    else:
        break
    if b == 0:
        break

if b % 2 == 0:
    print(sum(x))
else:
    b = 1
    x.sort()
    print(sum(x) - 2 * x[0])
