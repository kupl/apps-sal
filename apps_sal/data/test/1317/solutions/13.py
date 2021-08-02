n, k = map(int, input().split(' '))


def calc(x):
    m = n + x
    return (m // k)


total = 0
for i in range(k):
    for j in range(k):
        if ((i**2 + j**2) % k) == 0:
            total += calc(i) * calc(j)

print(total)
