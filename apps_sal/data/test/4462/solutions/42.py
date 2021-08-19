N = int(input())
a = list(map(int, input().split()))
f = []
t = []
o = []
ans = 'No'
for i in a:
    if i % 4 == 0:
        f.append(i)
    elif i % 2 == 0:
        t.append(i)
    else:
        o.append(i)
if len(t) == 0:
    if len(o) <= len(f) + 1:
        ans = 'Yes'
elif len(o) <= len(f):
    ans = 'Yes'
print(ans)
