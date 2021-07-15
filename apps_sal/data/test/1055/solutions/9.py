n = int(input())
a = [int(x) for x in input().strip().split()]

ans, k = 1, 2
while k <= n:
    i = 0
    while i < n:
        flag = True
        for j in range(k - 1):
            if a[i + j] > a[i + j + 1]:
                flag = False
                break
        if flag:
            ans = k
        i += k
    k = k * 2

print(ans)
