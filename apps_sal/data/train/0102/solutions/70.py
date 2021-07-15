s = int(input())
for _ in range(s):
    n = int(input())
    ans = 0
    for i in range(1, 10):
        k = 1
        while int(str(i)*k) <= n:
            k += 1
            ans += 1
    print(ans)

