n = int(input())
f = []
ans = 1
f.append(1)
f.append(2)
while f[ans] < n:
    f.append(f[ans] + f[ans - 1])
    ans += 1
if f[ans] == n:
    print(ans)
else:
    print(ans - 1)
