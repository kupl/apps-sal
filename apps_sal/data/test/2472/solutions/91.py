c = 0
D = 1
for a, b in sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x: x[1]):
    c += a
    if b < c:
        D = 0

print('Yes' if D else 'No')
