for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l1 = sorted(l)
    l2 = []
    mi = l1[0]
    ans = 0
    for i in range(n):
        if l[i] % mi != 0:
            if l1[i] != l[i]:
                ans = 1
                break
    if ans == 0:
        print("YES")
    else:
        print("NO")
