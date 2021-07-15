n = int(input())
l = []
m = []
ans = -10**9

for i in range(n):
    f = "".join(input().split())
    f = int(f, 2)
    l.append(f)

for i in range(n):
    p = list(map(int, input().split()))
    m.append(p)

for i in range(1, 2**10):
    ref = 0
    for j in range(n):
        cnt = bin(i & l[j]).count("1")
        ref += m[j][cnt]
    else:
        ans = max(ans, ref)

print(ans)
