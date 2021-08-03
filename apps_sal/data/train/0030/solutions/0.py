t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    ans = 0
    for y in range(1, n):
        if s[y] == s[y - 1]:
            ans += 1
    print((ans + ans % 2) // 2)
