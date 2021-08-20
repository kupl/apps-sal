n = int(input())
ans = list(input())
for i in range(n - 1):
    s = list(input())
    t = []
    for j in ans:
        if j in s:
            s.remove(j)
            t.append(j)
    ans = t
ans.sort()
print(''.join(ans))
