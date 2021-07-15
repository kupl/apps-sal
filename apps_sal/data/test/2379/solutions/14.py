n, k, c = map(int, input().split())
s = list(input())

count = 0

l, r = [], []

for i in range(n):
    m = i + c * count
    if m >= n:
        break
    if s[m] == 'o':
        count += 1
        if count > k:
            break
        l.append(m)

count = 0

for i in range(n - 1, -1, -1):
    m = i - c * count
    if m < 0:
        break
    if s[m] == 'o':
        count += 1
        if count > k:
            break
        r.append(m)

l.sort()
r.sort()

for i in range(k):
    if l[i] == r[i]:
        print(l[i] + 1)
