(n, m) = list(map(int, input().split()))
a = [0] * n
for i in range(m):
    s = list(map(int, input().split()))
    for j in range(1, 4):
        if a[s[j - 1] - 1] != 0:
            a[s[a[s[j - 1] - 1] - 1] - 1] = j
        else:
            a[s[j - 1] - 1] = j
print(' '.join(map(str, a)))
