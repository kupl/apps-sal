__author__ = 'Deepak'
(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
m = 1
d = []
while m <= len(a):
    for j in range(len(a) - m + 1):
        d.append(sum(list(a[j:j + m])))
    m += 1
d.sort(reverse=True)
for i in range(k):
    print(d[i], end=' ')
