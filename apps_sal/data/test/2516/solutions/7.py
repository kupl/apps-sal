n, p = map(int, input().split())
s = input()
if p == 2 or p == 5:
    ans = 0
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += i + 1
    print(ans)
else:
    di = {0: 1}
    tmp = 0
    for i in range(n):
        tmp += int(s[n - i - 1]) * pow(10, i, p)
        tmp %= p
        if tmp in di:
            di[tmp] += 1
        else:
            di[tmp] = 1
    ans = 0
    for i in di.values():
        ans += i * (i - 1) // 2
    print(ans)
