n = int(input())
l = []
for i in range(n):
    (k, h) = input().split()
    l.append([k, i + 1])
    l.append([h, i + 1])
a = list(map(int, input().split()))
l.sort()
cur = 0
ind = 0
ans = 'YES'
while ind < 2 * n and cur < n:
    while l[ind][1] != a[cur]:
        ind += 1
        if ind >= 2 * n:
            ans = 'NO'
            break
    cur += 1
print(ans)
