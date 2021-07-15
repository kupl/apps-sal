f = open('input.txt', 'r')
n = int(f.readline())
c = sorted(map(int, f.readline().split()))
j, v = 0, n - 1
for i in range(n):
    while j < n - 1 and 2 * c[i] >= c[j + 1]:
        j += 1
    v = min(v, n + i - j - 1)
open('output.txt', 'w').write(str(v))
