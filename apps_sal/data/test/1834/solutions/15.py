n = int(input())
a = sorted(map(int, input().split()))  # List

for i in range(1, len(a)):
    if (i + 1) % 2 == 0:
        if a[i] < a[i - 1]:
            temp = a[i]
            a[i] = a[i - 1]
            a[i - 1] = temp
            #i = 1
    else:
        if a[i] > a[i - 1]:
            temp = a[i]
            a[i] = a[i - 1]
            a[i - 1] = temp
            #i = 1

for i in range(n):
    print(a[i], end=" ")
print()
