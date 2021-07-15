a, b = input(), input()
i, j = 0, 0
while True:
    while j < len(b) and a[i] != b[j]: j += 1
    if j == len(b): break
    i += 1
    j += 1
print(i + 1)
