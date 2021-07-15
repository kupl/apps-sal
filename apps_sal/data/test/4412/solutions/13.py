q = int(input())
ans = []
for w in range(q):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    a = a[::-1]
    a1 = 0
    b1 = 0
    c1 = 0
    a1 = a[0]
    for i in range(n):
        if a1 % a[i] != 0:
            b1 = a[i]
            break
    for i in range(n):
        if a1 % a[i] != 0 and b1 % a[i] != 0:
            c1 = a[i]
            break
    a2 = 0
    b2 = 0
    c2 = 0
    if a1 % 2 == 0:
        for i in range(n):
            if a[i] == a1 // 2:
                a2 = a[i]
                break
    if a1 % 3 == 0:
        for i in range(n):
            if a[i] == a1 // 3:
                b2 = a[i]
                break
    if a1 % 5 == 0:
        for i in range(n):
            if a[i] == a1 // 5:
                c2 = a[i]
                break
    ans.append(max(a1 + b1 + c1, a2 + b2 + c2))
for i in range(q):
    print(ans[i])


