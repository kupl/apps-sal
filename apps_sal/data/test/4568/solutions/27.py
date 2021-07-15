n = int(input())
s = input()
c = 0
for i in range(n-1):
    xy=set(s[i+1:])&set(s[:i+1])
    c = max(c,len(xy))
print(c)
