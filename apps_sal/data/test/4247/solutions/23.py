n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(1, n - 1):
    l = [p[i - 1], p[i], p[i + 1]]
    if l[1] == sorted(l)[1]:
        cnt += 1
print(cnt)
