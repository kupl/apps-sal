3
n, k = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))

a.sort()
print(sum(a[i] for i in range(k)))
