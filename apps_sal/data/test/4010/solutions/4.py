
t = int(input())

for loop in range(t):

    n = int(input())

    a = list(map(int, input().split()))

    lis = [None] * (n + 1)

    ans = "NO"
    for i in range(n):

        if lis[a[i]] == None:
            lis[a[i]] = i
        elif lis[a[i]] + 1 < i:
            ans = "YES"
            break

    print(ans)
