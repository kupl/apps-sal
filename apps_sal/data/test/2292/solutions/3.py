q = int(input())
for _ in range(q):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    x1 = 0
    x2 = 0
    if n % 2 == 1:
        x1 = l1.pop(n // 2)
        x2 = l2.pop(n // 2)
    if x1 != x2:
        print("No")
    else:
        if n % 2 == 1:
            n -= 1
        d1 = []
        d2 = []
        for i in range(n // 2):
            d1.append([min(l1[i], l1[n - i - 1]), max(l1[i], l1[n - i - 1])])
            d2.append([min(l2[i], l2[n - i - 1]), max(l2[i], l2[n - i - 1])])
        d1.sort()
        d2.sort()
        if d1 == d2:
            print("Yes")
        else:
            print("No")
