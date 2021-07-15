n, k = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
if k > 1:
    print("Yes")
else:
    a[a.index(0)] = b[0]
    for i in range(1, n):
        if a[i] <= a[i - 1]:
            print("Yes")
            break
    else:
        print("No")
