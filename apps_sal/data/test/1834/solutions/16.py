n = int(input())
a = sorted(map(int,input().split()))

for i in range(1, len(a)):
    if (i+1)%2 == 0:
        if a[i] < a[i-1]:
            temp = a[i]
            a[i] = a[i-1]
            a[i-1] = temp
    else:
        if a[i] > a[i-1]:
            temp = a[i]
            a[i] = a[i-1]
            a[i-1] = temp

for i in range(n):
    print(a[i], end=" ")
print()

