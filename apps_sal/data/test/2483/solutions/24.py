def Csum(a):
    b, c = [0], 0
    for i in range(len(a)):
        c += a[i]
        b.append(c)
    return b


n, c = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [[0] * (10**5 + 10) for i in range(c)]
for i in a:
    b[i[2] - 1][i[0] - 1] += 1
    b[i[2] - 1][i[1]] -= 1
b = [Csum(i) for i in b]
ans = []
for i in range(10**5 + 10):
    d = 0
    for j in range(c):
        if b[j][i] > 0:
            d += 1
    ans.append(d)
print(max(ans))
