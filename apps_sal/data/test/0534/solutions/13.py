(n, t) = [int(i) for i in input().split()]
a = [i for i in input().strip()]
for i in range(t):
    falg = 1
    for j in range(n - 1):
        falg -= 1
        if a[j] == 'B' and a[j + 1] == 'G' and (falg <= 0):
            (a[j], a[j + 1]) = (a[j + 1], a[j])
            falg = 2
print(''.join(a))
