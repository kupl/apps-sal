import sys
(n, k) = [int(x) for x in sys.stdin.readline().split()]
j = 0
result = []
for i in range(n, 0, -1):
    if j < k:
        result.append(str(i))
        j += 1
    else:
        break
for i in range(1, n - k + 1):
    result.append(str(i))
print(' '.join(result))
