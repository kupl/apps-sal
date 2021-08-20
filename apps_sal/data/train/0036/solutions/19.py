n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
qq = sorted(q)
ans = dict()
limit = 0
i = 0
for k in qq:
    while not limit < k <= limit + a[i]:
        limit += a[i]
        i += 1
    ans[k] = i + 1
for k in q:
    print(ans[k])
