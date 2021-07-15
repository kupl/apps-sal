n=int(input())
s=input()
for i in range(0,n-3):
    if i==0:
        ans=min(abs(ord('A')-ord(s[i])),26-abs(ord('A')-ord(s[i]))) +min(abs(ord('C')-ord(s[i+1])),26-abs(ord('C')-ord(s[i+1]))) +min(abs(ord('T')-ord(s[i+2])),26-abs(ord('T')-ord(s[i+2]))) +min(abs(ord('G')-ord(s[i+3])),26-abs(ord('G')-ord(s[i+3])))
    else :
        ans=min(ans,min(abs(ord('A')-ord(s[i])),26-abs(ord('A')-ord(s[i]))) +min(abs(ord('C')-ord(s[i+1])),26-abs(ord('C')-ord(s[i+1]))) +min(abs(ord('T')-ord(s[i+2])),26-abs(ord('T')-ord(s[i+2]))) +min(abs(ord('G')-ord(s[i+3])),26-abs(ord('G')-ord(s[i+3]))))
print(ans)

