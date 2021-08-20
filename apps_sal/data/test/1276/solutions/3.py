(n, s) = (int(input()), input())
c = s.count('R') * s.count('G') * s.count('B')
for i in range(n + 1):
    for j in range(i, n + 1):
        k = 2 * j - i
        if k < n:
            if s[i] != s[j] and s[j] != s[k] and (s[i] != s[k]):
                c -= 1
print(c)
