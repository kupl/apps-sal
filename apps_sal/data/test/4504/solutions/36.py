s=input()
n=len(s)
for i in range(1,n):
    if s[:n-i]==s[:(n-i)//2]*2:
        print(n-i)
        break
