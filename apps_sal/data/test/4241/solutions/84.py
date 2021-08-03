s = str(input())
t = str(input())
ans = 10000

for i in range(len(s) - len(t) + 1):
    tmp = 0
    u = s[i:i + len(t)]
    for j in range(len(t)):
        if u[j] != t[j]:
            tmp += 1
    ans = min(ans, tmp)
print(ans)
