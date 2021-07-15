q = int(input())
a = [0] * (10 ** 5)
for i in range(1, 10 ** 5, 2):
    if (i + 1) // 2 % 2 == 0:
        pass
    else:
        for j in range(2, int((i)**(1 / 2)) + 1):
            if i % j == 0:
                break
        else:
            k = (i + 1) // 2
            for j in range(2, int((k)**(1 / 2)) + 1):
                if k % j == 0:
                    break
            else:
                a[i] = 1

for i in range(1, 10 ** 5):
    a[i] = a[i - 1] + a[i]
a[1] = 0
a[2] = 0

for i in range(q):
    l, r = list(map(int, input().split()))
    print((a[r] - a[l - 1]))

