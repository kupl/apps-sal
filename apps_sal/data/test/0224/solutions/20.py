s = 'A' + input() + 'A'
G = {'A', 'E', 'I', 'O', 'U', 'Y'}
ans = 1
t = 0
for i in s:
    if i not in G:
        t += 1
        if t > ans:
            ans = t
    else:
        t = 1
print(ans)
