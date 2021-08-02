l = list(map(int, input().split()))
k = int(input())
l.sort(reverse=True)
for i in range(k):
    l[0] *= 2
print(sum(l))
