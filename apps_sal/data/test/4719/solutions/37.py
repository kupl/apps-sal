n = int(input())
s = sorted([list(input()) for _ in range(n)], key=len)
ans = []
for i in s[0]:
    t = float('inf')
    for j in s:
        t = min(t, j.count(i))
    ans.append(i * t)
ans = sorted(list(set(ans)))
print(''.join(ans))
