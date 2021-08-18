import sys

reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

n = int(input())
a = list(map(int, input().split()))
digits = [[] for _ in range(32)]
for i, val in enumerate(a):
    shift = 0
    while val > 0:
        if val & 1:
            digits[shift].append(i)
        val >>= 1
        shift += 1

for i in reversed(list(range(32))):
    if len(digits[i]) == 1:
        idx = digits[i][0]
        a[0], a[idx] = a[idx], a[0]
        break

print(*a)
