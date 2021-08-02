import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
a = list(map(int, sys.stdin.readline().strip().split()))

amb = 0
h = [0] * (n + 1)
ha = [0] * (n + 1)
har = [0] * (n + 1)
hard = [0] * (n + 1)

for i in range(1, n + 1):
    if s[i - 1] == 'h':
        h[i] = h[i - 1] + a[i - 1]
    else:
        h[i] = h[i - 1]
    if s[i - 1] == 'a':
        ha[i] = min([ha[i - 1] + a[i - 1], h[i - 1]])
    else:
        ha[i] = ha[i - 1]
    if s[i - 1] == 'r':
        har[i] = min([har[i - 1] + a[i - 1], ha[i - 1]])
    else:
        har[i] = har[i - 1]
    if s[i - 1] == 'd':
        hard[i] = min([hard[i - 1] + a[i - 1], har[i - 1]])
    else:
        hard[i] = hard[i - 1]

print(hard[n])
