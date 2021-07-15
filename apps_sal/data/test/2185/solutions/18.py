t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ans = []
    for i in range(n):
        if a[i] != b[i]:
            ans.append(i)
    f = False
    for i in range(1, len(ans)):
        if ans[i] - ans[i - 1] != 1:
            f = True
    if f:
        print("NO")
    else:
        if len(ans) == 0:
            print("YES")
        else:
            f = False
            now = a[ans[0]] - b[ans[0]]
            for i in range(1, len(ans)):
                if now != a[ans[i]] - b[ans[i]]:
                    f = True
            if f or now > 0:
                print("NO")
            else:
                print("YES")
