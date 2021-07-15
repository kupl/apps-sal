n = int(input())
for i in range(n):
    a = sorted(list(map(int, input().split())))
    if a[2] >= a[0]+a[1]:
        print(a[0]+a[1])
    else:
        print(a[2]+(a[0]+a[1]-a[2])//2)
