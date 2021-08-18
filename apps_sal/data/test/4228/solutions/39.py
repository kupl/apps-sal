N, L = map(int, input().split())

nums = list(range(1, N + 1))
tasts = [L + num - 1 for num in nums]

abs_tasts = list(map(abs, tasts))
index = abs_tasts.index(min(abs_tasts))
tasts.pop(index)

print(sum(tasts))
