(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
com = []
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        com.append(sum(a[i:j]))
com = sorted(com, reverse=True)
for i in com[:k]:
    print(i, end=' ')
print('')
