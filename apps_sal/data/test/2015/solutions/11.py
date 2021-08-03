t = int(input())
for ii in range(t):
    a = list(map(int, input().split()))
    a = sorted(a)

    if a[2] <= a[1] + a[0] + 1:
        print("Yes")
    else:
        print("No")
