s = input()
ans = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if all("ACGT".count(c) == 1 for c in s[i:j + 1]):
            ans = max(ans, j - i + 1)
print(ans)
