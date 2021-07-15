n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n-1):
    b.append(a[i]+a[i+1])
b.append(a[n-1])
for i in b:
    print(i, end = ' ')
