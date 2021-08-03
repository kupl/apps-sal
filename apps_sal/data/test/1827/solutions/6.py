n = int(input())
a = list(map(int, input().split()))
l = sum(a) // n
a.sort()
for i in range(n):
    print(a[i], l - a[i])
