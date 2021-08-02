T = int(input())
for case in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    flag = 1
    for i in range(n - 1):
        if a[i] <= a[i + 1]:
            flag = 0
            break
    if flag:
        print("NO")
    else:
        print("YES")
