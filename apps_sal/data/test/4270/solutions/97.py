n = int(input())
a = sorted(map(int, input().split()))
c = a[0]
for i in range(1, n):
    c = (c + a[i]) / 2
print(c)
