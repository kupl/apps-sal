s = input().strip('0')
print('YES' if all(s[i] == s[-1 - i] for i in range(len(s))) else 'NO')
