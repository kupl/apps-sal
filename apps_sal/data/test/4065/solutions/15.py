n = int(input())
a = [int(x) for x in input().split()]
l = 1
max_l = 1
for i in range(n-1):
    if a[i+1] > a[i]*2:
        l = 1
    else:
        l += 1
        max_l = max(max_l, l)
print(max_l)

