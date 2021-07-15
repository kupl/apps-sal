import collections as c

n = int(input())
s = list(map(int,input().split()))
s = c.Counter(s)
ans = 0
for i in s.items():
    a = i[0]
    b = i[1]
    if b<a:
        ans += b
    else:
        ans += b-a
print(ans)
