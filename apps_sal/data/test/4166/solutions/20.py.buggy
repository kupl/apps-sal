n, m = map(int, input().split())

ans = [0] * (n)

for i in range(m):
    a = list(map(int, input().split()))
    if n >= 2:
        if a[0] == 1:
            if a[1] == 0:
                print("-1")
                return

    a[0] -= 1
    if ans[a[0]] == 0 or ans[a[0]] == a[1]:
        ans[a[0]] = a[1]
    else:
        print("-1")
        return

if n >= 2:
    for i in range(n):
        if ans[0] == 0:
            ans[0] = 1
            print(ans[i], end="")

        else:
            print(ans[i], end="")
else:
    print(ans[0])
