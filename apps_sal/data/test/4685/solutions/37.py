l = list(map(int, input().split()))
k = int(input())
for i in range(k):
    a = max(l)
    i = l.index(a)
    l[i] = l[i] * 2

print(sum(l))
