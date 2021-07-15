alphavit=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=input()
k=int(input())
a=input().split()
summ=0
for i in range(len(s)):
  work=alphavit.index(s[i])
  summ+=int(a[work])*(i+1)
maxa=0
for i in range(26):
  a[i]=int(a[i])
  if a[i]>maxa:
    maxa=a[i]
for i in range(len(s),len(s)+k):
  summ+=maxa*(i+1)
print(summ)



