a = '<3'
for _ in range(int(input())):
    a += input() + '<3'
b = input()
i, j, c, d = 0, 0, len(a), len(b)
while i < c and j < d:
    if a[i] == b[j]:
        i += 1
        j += 1
    else:
        j += 1
print(['no', 'yes'][i == c])
