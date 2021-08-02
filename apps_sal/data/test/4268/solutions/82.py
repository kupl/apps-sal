n, d = list(map(int, input().split()))
p = [[int(i) for i in input().split()] for y in range(n)]


def how_far(a, b):
    x = 0
    for s in range(0, d):
        x += (a[s] - b[s]) ** 2
    x = x ** (1 / 2)
    return x


count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        kyori = how_far(p[i], p[j])
        true_kyori = int(kyori)
        if kyori == true_kyori:
            count += 1

print(count)
