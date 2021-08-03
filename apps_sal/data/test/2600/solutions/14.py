
tt = int(input())

for loop in range(tt):

    n, m = list(map(int, input().split()))

    z = [0] * ((n + m - 1) // 2)
    o = [0] * ((n + m - 1) // 2)

    for i in range(n):

        a = list(map(int, input().split()))

        for j in range(m):

            d = min(i + j, n - i - 1 + m - j - 1)
            if d < len(z):

                if a[j] == 0:
                    z[d] += 1
                else:
                    o[d] += 1

    ans = 0
    for i in range(len(z)):
        ans += min(o[i], z[i])
    print(ans)
