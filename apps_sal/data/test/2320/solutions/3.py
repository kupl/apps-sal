t = int(input())
for h in range(t):
    ans = 1000000000
    n = int(input())
    a = str(input())
    b = str(input())
    if sorted(a) != sorted(b):
        ans = -1
    else:
        ans = 10000000000000
        for i in range(n):
            k = i
            count = 0
            for j in range(n):
                if k < n and a[j] == b[k]:
                    k += 1
                    count += 1
            ans = min(ans, n - count)
    print(ans)
