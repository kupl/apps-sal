t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d1 = False
    d2 = False
    ans = True
    for j in range(n):
        if a[j] > b[j]:
            if not d1:
                ans = False
        if a[j] < b[j]:
            if not d2:
                ans = False
        if a[j] == -1:
            d1 = True
        elif a[j] == 1:
            d2 = True
    if ans:
        print("YES")
    else:
        print("NO")
