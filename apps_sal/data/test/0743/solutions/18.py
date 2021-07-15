k = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)
for i in range(1000):
    for i in range(k-1):
        if (l[i+1] < l[i]):
            l[i] -= l[i+1]
            l.sort(reverse=True)
print(sum(l))

