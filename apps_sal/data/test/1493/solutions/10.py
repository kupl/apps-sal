n, m = list(map(int, input().split()))
for i in range(0, n):
    s = input()
    ans = ""
    for j in range(0, m):
        if s[j] == '.':
            if i % 2 == j % 2:
                ans += "B"
            else:
                ans += "W"
        else:
            ans += '-'
    print(ans)
