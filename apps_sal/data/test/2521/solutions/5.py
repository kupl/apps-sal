n = int(input())
a = list(map(int, input().split()))

b = list(enumerate(a))

l = sorted(b[:2*n], key=lambda x: x[1], reverse=True)
r = sorted(b[n:], key=lambda x: x[1])

big = [0] * (3*n)
small = [0] * (3*n)

for i, (pos, z) in enumerate(l):
    big[pos] = i
for i, (pos, z) in enumerate(r):
    small[pos] = i

first = sum(a[:n])
second = 0
for pos, z in r[:n]:
    second += z
i = 2 * n
j = n-1
ans = first - second
for split in range(n, 2*n):
    if big[split] < i:
        first += a[split]
        i -= 1
        while l[i][0] > split:
            i -= 1
        first -= l[i][1]
    if small[split] <= j:
        second -= a[split]
        j += 1
        while r[j][0] < split:
            j += 1
        second += r[j][1]
    ans = max(ans, first - second)
print(ans)
