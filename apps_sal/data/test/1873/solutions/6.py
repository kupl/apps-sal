from collections import Counter
n, m = list(map(int, input().split()))
c = Counter(list(map(int, input().split())))
a = list(c.keys())
print(sum(c[a[i]] * c[a[j]] for i in range(len(a) - 1) for j in range(i + 1, len(a))))


