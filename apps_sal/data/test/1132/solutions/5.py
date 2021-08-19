(n, m) = (int(x) for x in input().split())
cnt = [0] * n
for i in range(m):
    (u, v) = (int(x) for x in input().split())
    cnt[u - 1] += 1
    cnt[v - 1] += 1
if cnt.count(1) == n - 1:
    print('star topology')
elif cnt.count(2) == n:
    print('ring topology')
elif cnt.count(1) == 2 and cnt.count(2) == n - 2:
    print('bus topology')
else:
    print('unknown topology')
