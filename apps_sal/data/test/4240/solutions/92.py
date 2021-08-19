s = list(input())
t = list(input())
ans = 'No'
for _ in s:
    tmp = s.pop()
    s.insert(0, tmp)
    ''.join(s)
    if s == t:
        ans = 'Yes'
        break
print(ans)
