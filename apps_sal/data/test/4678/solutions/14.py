n = int(input())
a = [int(s) for s in input().split()]
allsum = sum(a)
for i in range(1, n):
    if a[i] < a[i - 1]:
        a[i] = a[i - 1]
print(sum(a) - allsum)
