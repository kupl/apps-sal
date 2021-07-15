n = int(input())
a = list(map(int,input().split()))
k = 0
pol = 0
for i in range(n):
    if a[i] < 0:
        if pol <= 0:
            k += 1
        else:
            pol -= 1
    else:
        pol += a[i]
print(k)
