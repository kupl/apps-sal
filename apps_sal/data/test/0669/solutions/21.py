n, m = list(map(int, input().split()))
l = [int(i) for i in input().split()]
first = l[:n // 2]
sec = l[n // 2:]
n1 = n // 2
n2 = n // 2 + n % 2
t1 = (1 << n1)
t2 = (1 << n2)
s1 = []
for i in range(t1):
    now = 0
    for j in range(len(first)):
        if i & (1 << j):
            now += first[j]
    s1.append(now % m)
s2 = []
for i in range(t2):
    now = 0
    for j in range(len(sec)):
        if i & (1 << j):
            now += sec[j]
    s2.append(now % m)
s1.sort()
s2.sort()
maxi = 0


def check(l, x):  # largest number less than x in l  # l is asc
    lo = 0
    hi = len(l) - 1
    ans = 0
    while lo <= hi:
        mi = (lo + hi) >> 1
        if l[mi] < x:
            ans = l[mi]
            lo = mi + 1
        else:
            hi = mi - 1
    return ans


for i in s1:
    req = m - i
    pair = check(s2, req)
    maxi = max(maxi, (i + pair) % m)
print(maxi)
