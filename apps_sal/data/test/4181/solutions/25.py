n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
num = 0
for i in range(n):
    min_ab = min(a[i],b[i])
    num += min_ab
    a[i] -= min_ab
    b[i] -= min_ab
    if b[i] != 0:
        min_ab = min(a[i + 1],b[i])
        num += min_ab
        a[i + 1] -= min_ab
        b[i] -= min_ab
print(num)
