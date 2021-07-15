read = lambda: map(int, input().split())
n = int(input())
a = sorted(read())
k = 1
for i in range(n):
    if a[i] > k:
        a[i] = k
        k += 1
    elif a[i] == k:
        k += 1
print(k)
