s= input()
a = [0]*len(s)
print(len(a)-s[1::2].count('0')-s[::2].count('1') if s[0]=='1' else len(a)-s[1::2].count('1')-s[::2].count('0'))
