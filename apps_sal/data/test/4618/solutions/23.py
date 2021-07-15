s = input()
k = int(input())
n = len(s)

# print('s',s,'k',k)
c = set()
for i in range(n):
    # print(s[i:i+5])
    t = s[i:i+5]
    for j in range(1,5+1):
        # print(t[:j])
        c.add(t[:j])

c = list(c)
c.sort()
# print(*c,sep='\n')
print((c[k-1]))

