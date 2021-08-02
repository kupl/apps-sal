t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    flag = False
    for i in range(n - 1):
        if a[i] + 1 == a[i + 1]:
            flag = True
    if flag:
        print(2)
    else:
        print(1)
