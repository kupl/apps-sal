(a, b) = list(map(str, input().split()))
an = -1
for i in range(len(a)):
    for j in range(len(b)):
        c = int(i == -1) + int(j == -1)
        if an == -1 or a[0:i + 1] + b[0:j + 1] < an:
            an = a[0:i + 1] + b[0:j + 1]
print(an)
