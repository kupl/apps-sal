n = int(input())
a = list(map(int, input().split()))
while 1:
    T = True
    for i in range(n):
        for j in range(n):
            if a[i] > a[j]:
                a[i] = a[i] - a[j]
                T = False
            elif a[i] < a[j]:
                a[j] = a[j] - a[i]
                T = False
    if T:
        break
print(sum(a))
