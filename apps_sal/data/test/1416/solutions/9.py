

n, w = list(map(int, input().split()))

cups = sorted(list(map(int, input().split())))

girl_cap = min(cups[0], cups[n] / 2)


print(min(girl_cap * 3 * n, w))
