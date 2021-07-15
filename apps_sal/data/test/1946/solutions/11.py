d = {}
n = int(input())
for i in range(n):
    j, k = list(map(int, input().split()))
    d[j] = k

m = int(input())
for i in range(m):
    j, k = list(map(int, input().split()))
    if j in d:
        d[j] = max(d[j], k)
    else:
        d[j] = k

ss = 0
for i, v in d.items():
    # print(i, v)
    ss += v
print(ss)
