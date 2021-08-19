n = int(input())
f = [list(map(int, input().split())) for i in range(n)]
p = [list(map(int, input().split())) for i in range(n)]
ans = -10 ** 10
for i in range(1, 1024):
    bit = bin(i)[2:].zfill(10)
    a = 0
    for j in range(n):
        b = 0
        for k in range(10):
            if int(bit[k]) and f[j][k]:
                b += 1
        a += p[j][b]
    ans = max(ans, a)
print(ans)
