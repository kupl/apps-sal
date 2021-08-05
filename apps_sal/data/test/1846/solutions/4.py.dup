f = open('input.txt', 'r')
n, a = int(f.readline()), list(map(int, f.readline().split()))
an, ap = [0] * n, [0] * n
for i in range(1, n):
    an[i] = an[i - 1] + (a[i - 1] >= 0)
for i in range(n - 2, -1, -1):
    ap[i] = ap[i + 1] + (a[i + 1] <= 0)
print(min(an[i + 1] + ap[i] for i in range(n - 1)), file=open('output.txt', 'w'))
