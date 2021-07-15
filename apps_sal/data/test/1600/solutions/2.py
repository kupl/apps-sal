n = int(input())
s = input().split()
a = [[0] * 2 for i in range(n)]

for i in range(n):
    a[i][0] = int(s[i])
    a[i][1] = i

a.sort()


if (a[0][1] == n-1 or a[n-1][1] == 0):
    print(1)
else:
    sum = 0
    res = 0
    ans = 0
    for i in range(n):
        sum += a[i][1]
        res += i
        if sum == res:
            ans += 1

    print(ans)

