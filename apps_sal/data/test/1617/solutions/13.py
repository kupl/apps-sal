t = 1
for test in range(t):
    n = int(input())
    ans = set()
    ans.add(1)
    ans.add((n * (n + 1)) // 2)
    for i in range(2, int(pow(n, 0.5)) + 2):
        if n % i == 0:
            tmp = n // i
            tmp2 = tmp * (2 + ((tmp - 1) * i))
            ans.add(tmp2 // 2)
            tmp2 = i * (2 + ((i - 1) * tmp))
            ans.add(tmp2 // 2)
    print(*sorted(list(ans)))
