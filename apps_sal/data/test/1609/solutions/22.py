n = int(input())
a = list(map(int, input().split()))
c = [0] * 100001
for ai in a:
    c[ai] += 1
b = [x for x in range(1, n + 1) if c[x] == 0]
j = 0
for (i, ai) in enumerate(a):
    if c[ai] > 1 or ai > n:
        a[i] = b[j]
        j += 1
        c[ai] -= 1
print(' '.join(map(str, a)))
