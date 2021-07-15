a, b = map(int, input().split())
diff = b - a
towers = [0] * diff
for i in range(1, diff):
    towers[i] = towers[i - 1] + i
print(towers[-1] - a)
