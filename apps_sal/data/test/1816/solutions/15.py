# n,p,q=map(int,input().split())
##
# s=input()
##
# l=list()
##
# while len(s):
# if len(s)%p!=0 and len(s)>=q:
# l.append(s[0:q])
# s=s[q:]
# elif len(s)%p==0 and len(s)>=p:
# l.append(s[0:p])
# s=s[p:]
# else:
# break
# if len(s):
# print(-1)
# else:
# print(len(l))
# for x in l:
# print(x)

n = input()
s = list(input().split())

i = 1
l = list()
for x in s:
    l.append((int(x), i))
    i += 1
l.sort()
ans = 0
for i in range(1, len(l)):
    ans += abs(l[i][1] - l[i - 1][1])

print(ans)
