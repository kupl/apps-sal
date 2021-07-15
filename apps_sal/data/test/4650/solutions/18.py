n = int(input())
for i in range(n):
    x = int(input())
    a = [int(i) for i in input().split()]
    zero = 0
    one = 0
    two = 0
    for i in range(x):
        if a[i] % 3 == 0:
            zero += 1
        elif a[i] % 3 == 1:
            one += 1
        else:
            two += 1
    print(zero + min(two, one) + (max(two, one) - min(two, one)) // 3)
