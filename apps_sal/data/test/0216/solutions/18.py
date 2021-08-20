n = int(input())
a = [int(x) for x in input().split()]
b = 0
c = 0
for i in range(len(a)):
    if a[i] < 0:
        c += a[i] * -1
    elif a[i] >= 0:
        b += a[i]
ans = b + c
print(ans)
