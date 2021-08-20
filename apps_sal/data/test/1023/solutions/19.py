(n, m, ta, tb, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = {}
i = 0
j = 0
while i < n and j < m:
    if b[j] >= a[i] + ta:
        d[i] = j
        i += 1
    else:
        j += 1
M = 0
for i in range(min(n, k) + 1):
    try:
        M = max(M, b[d[i] + k - i] + tb)
    except:
        M = -1
        break
print(M)
