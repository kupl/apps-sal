n = list(map(int, input().split()))
a = list(map(int, input().split()))
a.reverse()
mx = a[0]
ans = list()
ans.append(0)
for i in a[1:]:
    ans.append(max(0, mx - i + 1))
    mx = max(mx, i)
ans.reverse()
p = ''
for i in ans:
    p += i.__str__() + ' '
print(p)
