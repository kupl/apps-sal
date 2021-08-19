n = int(input())
s = list(input())
r = s.count('R')
g = s.count('G')
b = s.count('B')
ans = r * g * b
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if j - i + j < n:
            k = j - i + j
            if s[i] != s[j] and s[i] != s[k] and (s[j] != s[k]):
                ans -= 1
print(ans)
