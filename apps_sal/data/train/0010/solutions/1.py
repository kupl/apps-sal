
t = int(input())

for loop in range(t):

    n = int(input())
    p = list(map(int, input().split()))
    a = p

    ans = []

    for i in range(n):

        if i == 0 or i == n - 1:
            ans.append(p[i])

        elif a[i - 1] <= a[i] <= a[i + 1]:
            continue
        elif a[i - 1] >= a[i] >= a[i + 1]:
            continue
        else:
            ans.append(p[i])

    print(len(ans))
    print(*ans)
