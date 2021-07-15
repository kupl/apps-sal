s=list(input())
t=list(input())
n=len(s)
a=[s.count(chr(97+i)) for i in range(26)]
b=[t.count(chr(97+i)) for i in range(26)]
if all(a[ord(s[i])-97]==b[ord(t[i])-97] for i in range(n)):
    print("Yes")
else:
    print("No")


