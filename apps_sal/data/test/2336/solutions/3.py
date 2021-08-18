from sys import stdin, stdout


def read_ints():
    return list(map(int, stdin.readline().split()))


n, k, q = read_ints()

MAX_TEMP = 200000 + 10
temps = [0 for x in range(MAX_TEMP)]

for i in range(n):
    l, r = read_ints()
    temps[l] += 1
    temps[r + 1] -= 1

sums = [0 for x in range(MAX_TEMP)]
count = 0
for i in range(1, MAX_TEMP):
    count += temps[i]
    if count >= k:
        sums[i] = 1
    sums[i] += sums[i - 1]

for i in range(q):
    a, b = read_ints()
    print(sums[b] - sums[a - 1])
