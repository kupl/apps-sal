n = int(input())
a = list(map(int, input().split()))
maxx = -1
minn = -1
for i in range(n):
    if a[i] == maxx + 1:
        maxx = a[i]
    elif a[i] > maxx + 1:
        minn = i
        break
if minn == -1:
    print(minn)
else:
    print(minn + 1)
