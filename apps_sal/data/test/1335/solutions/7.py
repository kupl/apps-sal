n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [[0] for i in range(k)]
c = [0] * k
p = [0] * (150 * n + 1)
for i in a:
    m = 0
    for j in range(k):
        if c[j] < c[m]:
            m = j
    b[m].append(b[m][-1] + i)
    c[m] += i
    p[b[m][-1] + 1] += 1
for i in range(1, len(p)):
    p[i] += p[i - 1]
for i in range(len(p)):
    p[i] = (200 * p[i] + n) // (2 * n)
ans = 0
for i in range(k):
    for j in range(1, len(b[i])):
        l = b[i][j - 1]
        r = b[i][j]
        pp = l + 1
        while pp <= r:
            if p[pp] == pp - l:
                ans += 1
                #print(i, j)
                break
            pp += 1
print(ans)
#print(b, p, sep='\n')
