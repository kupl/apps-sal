n, m, k = list(map(int, input().split()))
a, c = [], 0
for i in range(m + 1):
    a.append(bin(int(input())).replace('0b', ''))
for i in range(m):
    s = str(int(a[m]) + int(a[i]))
    if s.count('1') <= k:
        c += 1
print(c)
