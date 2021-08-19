def C(k):
    return k * (k - 1) // 2


n = int(input())
r = [0 for i in range(n)]
c = [0 for i in range(n)]
for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == 'C':
            r[i] += 1
            c[j] += 1
ans = 0
for i in range(n):
    ans += C(r[i]) + C(c[i])
print(ans)
