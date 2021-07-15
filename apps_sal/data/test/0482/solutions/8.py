n, k = list(map(int, input().split()))
s = []
l = ""
for i in range(k):
    s.append(chr(97 + i))
for i in range(len(s)):
    l += s[i]
for i in range(n//k):
    print(l,end='')
for i in range(n%k):
    print(s[i],end='')
