(sl, s) = ('AHIMOTUVWXY', input())
print('YES' if all((s[i] in sl and s[i] == s[len(s) - i - 1] for i in range(len(s)))) else 'NO')
