from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    for j in range(i + 1, n):
        b.append(a[i] + a[j])
c = Counter(b)
x = -1
for i in c:
    x = max(x, c[i])
print(x)
