import sys
n = [int(d) for d in sys.stdin.readline()[:-1]]
for x in [1, 6, 8, 9]:
    for i in range(len(n)):
        if n[i] == x:
            del n[i]
            break
prefix = [1869, 6189, 1689, 6198, 1698, 9861, 1896]
L = sum([n[i] * pow(10, len(n) - i - 1, 7) for i in range(len(n))]) % 7
print(prefix[-L * pow(10, 5 * len(n), 7) % 7], end='')
print(*n, sep='')
