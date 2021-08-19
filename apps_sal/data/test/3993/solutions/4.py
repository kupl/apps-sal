(n, m, k) = map(int, input().split())
p = list(map(int, input().split()))
count = 0
delete = 0
now = 0
while now < m:
    up = ((p[now] - delete - 1) // k + 1) * k + delete
    while now < m and p[now] <= up:
        now += 1
        delete += 1
    count += 1
print(count)
