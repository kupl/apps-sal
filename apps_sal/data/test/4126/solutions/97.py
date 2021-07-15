s=input()
s1=s[:len(s)//2]
s2=s[len(s)//2+1:]
print('Yes' if s==s[::-1] and s1==s1[::-1] and s2==s2[::-1] else 'No')
