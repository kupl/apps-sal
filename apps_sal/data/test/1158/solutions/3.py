import collections
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = collections.Counter(a)
c = b.most_common(1)[0][1]
gg = max((c + k - 1) // k, 1)
need = k * gg * len(b)

for i in b:
    need -= b[i]


print(need)
