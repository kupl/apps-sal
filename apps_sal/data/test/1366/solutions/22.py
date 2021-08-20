n = int(input())
k = []
t = []
for i in range(n):
    (p, m) = map(int, input().split())
    k.append(p)
    t.append(m)
ans = n
for i in range(len(k)):
    for j in range(len(t)):
        if i == j:
            continue
        if k[i] == t[j]:
            ans -= 1
            break
print(ans)
