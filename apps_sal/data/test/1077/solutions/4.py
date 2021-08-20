(n, m) = list(map(int, input().split()))
count = [0] * (m + 1)
lother = []
lbig = []
a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i] <= m:
        count[a[i]] += 1
    else:
        lother.append(i)
for i in range(len(a)):
    if a[i] <= m and count[a[i]] > n // m:
        lbig.append(i)
        count[a[i]] -= 1
ans = 0
for i in range(1, m + 1):
    while count[i] < n // m:
        ans += 1
        if len(lother) != 0:
            a[lother[0]] = i
            lother.pop(0)
        else:
            a[lbig[0]] = i
            lbig.pop(0)
        count[i] += 1
print(str(n // m) + ' ' + str(ans))
for i in a:
    print(i, end=' ')
