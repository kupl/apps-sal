a = input()
mm = 0
for i in range(len(a)):
    for j in range(i, len(a)):
        x = ''
        for xx in range(i, j + 1):
            x += a[xx]
        if x != x[::-1]:
            mm = max(mm, len(x))
print(mm)
