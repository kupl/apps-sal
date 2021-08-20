L = int(input())
b = format(L, 'b')
n = len(b)
m = 2 * (n - 1) + b.count('1') - 1
print(n, m)
for i in range(1, n):
    print(i, i + 1, 0)
    print(i, i + 1, 2 ** (i - 1))
w = 2 ** (n - 1)
for j in range(20, -1, -1):
    if L - w >> j & 1:
        print(j + 1, n, w)
        w += 2 ** j
