from operator import itemgetter
N = int(input())
l = []
s = []
for i in range(1, N + 1):
    (k, v) = input().split()
    l.append([k, int(v), i])
    s.append(k)
l = sorted(l)
s = sorted(list(set(s)))
for t in s:
    for n in range(N - 1, -1, -1):
        (k, v, i) = l[n]
        if t == k:
            print(i)
