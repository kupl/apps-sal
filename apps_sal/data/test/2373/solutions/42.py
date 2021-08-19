n = int(input())
p = [int(x) for x in input().rstrip().split()]
cnt = 0
for i in range(n - 1):
    if p[i] == i + 1:
        now = p[i + 1]
        p[i + 1] = p[i]
        p[i] = now
        cnt += 1
if p[n - 1] == n:
    cnt += 1
print(cnt)
