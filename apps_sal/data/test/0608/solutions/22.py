def present(n, a):
    num = 0
    pr = 0
    for i in range(n):
        if a[i] == 4 or a[i] == 5:
            num += 1
        else:
            pr += (num // 3)
            num = 0
    pr += (num // 3)

    return pr


n = int(input())
a = [int(x) for x in input().split()]
print(present(n, a))
