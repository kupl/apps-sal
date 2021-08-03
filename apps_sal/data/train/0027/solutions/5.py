t = int(input())
for j in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    ans = 0
    for i in range(n):
        k = a[i]
        while k % 2 == 0 and k not in s:
            s.add(k)
            k = k // 2
            ans += 1
    print(ans)
