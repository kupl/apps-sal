(n, k) = list(map(int, input().split()))
d = []
a = []
for i in range(k):
    d.append(int(input()))
    a.append(list(map(int, input().split())))
lis = []
for i in range(k):
    for j in range(len(a[i])):
        lis.append(a[i][j])
lis = set(lis)
print(n - len(lis))
