n = int(input())
f = []
ans = -10 ** 9
for i in range(n):
    a = ''.join(input().split())
    a = int(a, 2)
    f.append(a)
p = [list(map(int, input().split())) for i in range(n)]
for i in range(1, 2 ** 10):
    ref = 0
    for j in range(n):
        cnt = bin(i & f[j]).count('1')
        ref += p[j][cnt]
    else:
        ans = max(ans, ref)
print(ans)
