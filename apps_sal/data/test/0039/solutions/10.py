s = input()
ans = 0
n = len(s)
for i in range(n):
    for j in range(i + 1, n + 1):
        c = s[i:j]
        if c != c[::-1] and j - i > ans:
            ans = j - i
print(ans)
