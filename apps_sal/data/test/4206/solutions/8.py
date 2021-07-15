s = [int(i) for i in input()]

count = 0
current = []
for h, i in enumerate(s):
    for j in range(len(current)):
        current[j] = current[j] * 10 + i
    current.append(i)
    if h + 1 < len(s) and s[h + 1] != 0:
        for m in current:
            if m % 3 == 0:
                count += 1
                current = []
                break
    else:
        for m in current:
            if m % 3 == 0:
                count += 1
                current = []
                break
print(count)

