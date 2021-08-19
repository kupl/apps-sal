n = int(input())
(s, t) = input().split()
ans = []
ss = list(s)
tt = list(t)
for i in range(n):
    ans.append(ss[i])
    ans.append(tt[i])
print(''.join(ans))
