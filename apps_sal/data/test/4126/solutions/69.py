s=input()
n=(len(s)-1)//2
print('Yes' if s[:n]==s[n+1:] else 'No')
