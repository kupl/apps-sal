from collections import Counter
(n, *v) = list(map(int, open(0).read().split()))
odd = [v[i] for i in range(0, n, 2)]
even = [v[i] for i in range(1, n, 2)]
o = Counter(odd)
e = Counter(even)
if o.most_common()[0][0] != e.most_common()[0][0]:
    print(n - o.most_common()[0][1] - e.most_common()[0][1])
else:
    a = n - o.most_common()[0][1] - max(sorted(e.values())[:-1] + [0])
    b = n - e.most_common()[0][1] - max(sorted(o.values())[:-1] + [0])
    print(min(a, b))
