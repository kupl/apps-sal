K, X = list(map(int, input().split()))

rocks = [rock for rock in range(-10000, 10001)]
blacks = list(rocks[X - K + 10001:X + K + 10000])
print((" ".join([str(rock) for rock in blacks])))

