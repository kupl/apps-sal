n = int(input())
while n != 0:
    n -= 1
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] >= a[2]:
        print(sum(a) // 2)
    else:
        print(a[0] + a[1])
