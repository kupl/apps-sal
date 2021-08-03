N, L = map(int, input().split(" "))

apple = [L + i - 1 for i in range(1, N + 1)]

abs_apple = list(map(abs, apple))

minimum_idx = abs_apple.index(min(abs_apple))

print(sum(apple) - apple[minimum_idx])
