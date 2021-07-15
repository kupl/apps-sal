f = open('input.txt', 'r')
n = int(f.readline())
arr = sorted(map(int, f.readline().split()))
j = 0
res = n - 1

for i in range(n):
    while j < n - 1 and 2 * arr[i] >= arr[j + 1]:
        j += 1
    res = min(res, n + i - j - 1)


open('output.txt', 'w').write(str(res))

