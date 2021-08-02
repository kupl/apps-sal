
t = int(input())

for loop in range(t):

    n = int(input())

    a = list(map(int, input().split()))

    ans = "YES"
    for i in range(n - 1):

        if a[-1] % 2 != a[i] % 2:
            ans = "NO"

    print(ans)
