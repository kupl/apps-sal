(n, m) = [int(x) for x in input().strip().split(' ')]
a = [int(x) for x in input().strip().split(' ')]
b = [int(x) for x in input().strip().split(' ')]
s = [1] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i - 1]
idx = 0
for i in range(m):
    while True:
        if b[i] < s[idx + 1]:
            print(idx + 1, b[i] - s[idx] + 1)
            break
        else:
            idx += 1
