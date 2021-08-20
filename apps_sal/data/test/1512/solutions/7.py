n = int(input().strip())
a = list(map(int, input().strip().split()))
isit = [0] * (n + 1)
isit[a[0]] = 1
freq = [0] * (n + 1)
m1 = [0] * n
m2 = [0] * n
m1[0] = a[0]
for i in range(1, n):
    if m1[i - 1] < a[i]:
        m1[i] = a[i]
        m2[i] = m1[i - 1]
    else:
        m1[i] = m1[i - 1]
        if m2[i - 1] < a[i]:
            m2[i] = a[i]
        else:
            m2[i] = m2[i - 1]
tot = 1
for i in range(1, n):
    if m1[i] > a[i]:
        if m2[i] == a[i]:
            freq[m1[i]] += 1
    else:
        tot += 1
        isit[a[i]] = 1
mx = 0
val = a[0]
for i in range(0, n):
    if mx < tot + freq[a[i]] - isit[a[i]]:
        val = a[i]
        mx = tot + freq[a[i]] - isit[a[i]]
    elif mx == tot + freq[a[i]] - isit[a[i]]:
        val = min(val, a[i])
print(val)
