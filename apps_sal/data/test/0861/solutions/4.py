m, r = list(map(int, input().split()))


def calc(k):
    if k < 1:
        return 0
    else:
        return (1 + 2 * (k - 1)) * 2**0.5 + k * 2 + (k - 1) * (k - 2)


avg = 0
div = m ** 2

for i in range(0, m):
    avg += r * (2 + calc(i) + calc(m - 1 - i)) / div

print(avg)
