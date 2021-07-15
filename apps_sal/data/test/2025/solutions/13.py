q = int(input())
a = [-1, -1, -1, -1, 1, -1, 1, -1, 2, 1, 2, -1]
for i in range(q):
    n = int(input())
    if n <= 11:
        print(a[n])
    else:
        ans = n // 4
        if n % 2 == 1:
            ans -= 1
        print(ans)

