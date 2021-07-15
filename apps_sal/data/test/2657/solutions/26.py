n = int(input())
a = list(map(int,input().split()))
a.sort()
l = a[-1]
x = l // 2
y = 10 ** 12
z = 0
for i in range(n-1):
    if y >= abs(x-a[i]):
        y = abs(x-a[i])
        z = i
print(l,a[z])
