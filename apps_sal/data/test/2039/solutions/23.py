n = int(input())

a = [int(i) for i in input().split()]
ex = []
for i in range(1, n-1):
    if a[i] > a[i-1] and a[i]>a[i+1]:
        ex += [a[i]]

    elif a[i] < a[i-1] and a[i] < a[i+1]:
        ex += [a[i]]
print(len(ex))
