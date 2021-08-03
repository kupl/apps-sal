s, t = 'CODEFORCES', input().strip()
print('YES' if any(s[:i] == t[:i] and s[i:] == t[len(t) - len(s) + i:] for i in range(len(s) + 1)) else 'NO')
