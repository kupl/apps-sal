import collections
n = int(input())
a = list(map(int, input().split()))
lis = []

for i in range(n-1):
    for j in range(i+1, n):
        lis.append(a[i] + a[j])

# print(lis)
# list.sort()
c = collections.Counter(lis)
print(c.most_common()[0][1])
