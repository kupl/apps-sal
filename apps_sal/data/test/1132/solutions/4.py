(n, m) = list(map(int, input().split()))
l = [0] * n
d = l[:]
for _ in range(m):
    (a, b) = list(map(int, input().split()))
    l[a - 1] += 1
    l[b - 1] += 1
for i in l:
    d[i] += 1
if d[1] == 2 and d[2] == n - 2:
    print('bus topology')
elif d[2] == n:
    print('ring topology')
elif d[1] == n - 1 and d[n - 1] == 1:
    print('star topology')
else:
    print('unknown topology')
