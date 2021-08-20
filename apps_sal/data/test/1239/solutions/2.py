n = int(input())
(*l,) = list(map(int, input().split()))
l.sort()
d = []
for i in range(n - 1):
    d.append(l[i + 1] - l[i])
print(min(d), d.count(min(d)))
