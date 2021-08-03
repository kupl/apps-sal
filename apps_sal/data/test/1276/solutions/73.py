n = int(input())
s = input()
ans = s.count("R") * s.count("G") * s.count("B")
for i in range(min(1, n // 3), ((n - 1) // 2) + 1):
    for j in range(n - (i * 2)):
        if s[j] != s[j + i] and s[j + i] != s[j + i + i] and s[j + i + i] != s[j]:
            ans -= 1
print(ans)
