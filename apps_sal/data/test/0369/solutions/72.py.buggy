n, m = list(map(int, input().split()))
s = list(map(int, list(input())))
ans = []
i = n
while i > 0:
    j = max(0, m - i)
    while s[i - (m - j)] != 0:
        j += 1
        if j == m:
            print((-1))
            return
    ans.append(m - j)
    i -= (m - j)
ans.reverse()
print((' '.join(map(str, ans))))
