n, k = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
max_i = 0
for i in range(k):
    if (n % a[i]) < (n % a[max_i]):
        max_i = i
print(max_i + 1, n // a[max_i], sep=' ')
