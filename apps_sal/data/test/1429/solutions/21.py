n, s = input().split()
n = int(n)
ans = 0

for i in range(n):
    AT, GC = 0, 0
    for j in range(i, n):
        if s[j] == 'A':
            AT += 1
        if s[j] == 'T':
            AT -= 1
        if s[j] == 'G':
            GC += 1
        if s[j] == 'C':
            GC -= 1
        if AT == 0 and GC == 0:
            ans += 1
print(ans)
