n = int(input())

a = list(map(int, input().split(' ')))


def sol(x):
    total = 0
    for i in range(1, n + 1):
        current = abs(i - 1) + abs(x - i) + abs(x - 1)
        current *= 2 * a[i - 1]
        total += current

    return total


maxV = 100000000

for i in range(n):
    maxV = min(sol(i + 1), maxV)

print(maxV)
