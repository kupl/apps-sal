n = int(input())
l = list(map(int, input().split()))
d = {}
s = set()
s.add(0)
d[0] = 1
ans = 1
for i in range(n):
    if l[i] in s:
        d[i + 1] = d[l[i]]
        s.remove(l[i])
        s.add(i + 1)
    else:
        s.add(i + 1)
        ans += 1
        d[i + 1] = ans
print(ans)
