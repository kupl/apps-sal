data = [2, 3, 5, 7]
n = int(input())
help = 0
for i in range(4):
    for j in range(4):
        if j > i:
            help += n // (data[i] * data[j])
print(n - (n // 2 + n // 3 + n // 5 + n // 7 - help + n // (2 * 3 * 5) + n // (2 * 3 * 7) + n // (5 * 7 * 3) + n // (5 * 7 * 2) - n // (2 * 3 * 5 * 7)))
