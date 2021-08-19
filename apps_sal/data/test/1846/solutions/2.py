fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n = int(fin.readline())
a = [int(i) for i in fin.readline().split()]
plus = [0] * (n + 1)
minus = [0] * (n + 1)
zero = [0] * (n + 1)
for i in range(n):
    if a[i] < 0:
        plus[i + 1] = plus[i]
        minus[i + 1] = minus[i] + 1
        zero[i + 1] = zero[i]
    elif a[i] > 0:
        plus[i + 1] = plus[i] + 1
        minus[i + 1] = minus[i]
        zero[i + 1] = zero[i]
    else:
        plus[i + 1] = plus[i]
        minus[i + 1] = minus[i]
        zero[i + 1] = zero[i] + 1
best = float('inf')
for i in range(n - 1):
    x = plus[i + 1] + minus[-1] - minus[i + 1] + zero[-1]
    best = min(best, x)
print(best, file=fout)
fin.close()
fout.close()
