(n, m) = map(int, input().split())
l = []
for i in range(n):
    p = list(map(int, input().split()))
    for j in range(1, p[0] + 1):
        l.append(p[j])
cnt = 0
for k in l:
    if l.count(k) == n:
        cnt += 1
print(cnt // n)
