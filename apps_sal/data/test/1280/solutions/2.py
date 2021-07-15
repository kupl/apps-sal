s = input()
a = input()
k = int(input())
S=sorted(s[i:] for i in range(len(s)))
p=''
r=0
for e in S:
    t=0
    s=0
    for i in range(len(e)):
        if i >= len(p) or e[i] != p[i]: 
          s=1
        if a[ord(e[i])-ord('a')]=='0':
          t+=1
        if t > k:
          break
        if s: 
          r+=1
    p = e
print(r)
