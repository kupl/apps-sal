n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))
count = 100000000000
for i in range(m - 1, -1, -1):
    if (i - n + 1) < 0:
        break
    else:
        count = min(count, A[i] - A[i - n + 1])
print(count)
