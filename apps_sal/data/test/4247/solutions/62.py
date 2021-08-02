n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(n - 2):
    l = [p[i], p[i + 1], p[i + 2]]
    l.sort()
    if p[i + 1] == l[1]:
        cnt += 1
print(cnt)
