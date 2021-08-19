(n, k, c) = map(int, input().split())
s = [i == 'o' for i in list(input())]
i = 0
cnt = 0
l = [0] * n
r = [0] * n
while i < n:
    if s[i]:
        cnt += 1
        for j in range(i, c + i + 1):
            if j < n:
                l[j] = cnt
        i += c + 1
    else:
        l[i] = cnt
        i += 1
i = n - 1
cnt = 0
while i >= 0:
    if s[i]:
        cnt += 1
        for j in range(i, i - 1 - c, -1):
            if j >= 0:
                r[j] = cnt
        i -= c + 1
    else:
        r[i] = cnt
        i -= 1
r.append(0)
if r[1] < k:
    print(1)
for i in range(1, n - 1):
    if not s[i]:
        continue
    if l[i - 1] + r[i + 1] < k:
        print(i + 1)
if l[n - 2] < k:
    print(n)
