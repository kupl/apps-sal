n, m = [int(i) for i in input().split()]
c1 = [int(i) for i in input().split()]
c1.sort()
ms = 0
i = 0
while i < n - 1:
    start = i
    while i < n - 1 and c1[i] == c1[i + 1]:
        i += 1
    ms = max(ms, i - start)
    i += 1
ms += 1
c2 = c1[-ms:] + c1[:-ms]
cnt = 0
for i in range(n):
    if c1[i] != c2[i]:
        cnt += 1
print(cnt)
for i in range(n):
    print(c1[i], c2[i])
