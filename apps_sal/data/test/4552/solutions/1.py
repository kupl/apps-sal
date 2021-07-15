n = int(input())
f = []
ans = -10**9

for i in range(n):
    a = input().split()
    f.append(a)

p = [list(map(int, input().split())) for i in range(n)]

for i in range(1, 2**10):
    ref = 0
    i = str(bin(i))[2:].zfill(10)
    for j in range(n):
        cnt = 0
        for k in range(10):
            if i[k] == f[j][k] == "1":
                cnt += 1
        ref += p[j][cnt]
    else:
        ans = max(ans, ref)

print(ans)
