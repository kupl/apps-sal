n = int(input())
m = [i for i in range(1, n)]
p = list(map(int, input().split()))
cnt = 0
for i in m:
    if p[i - 1] == i:
        p[i - 1] = p[i]
        p[i] = i
        cnt += 1
if p[-1] == n:
    cnt += 1
print(cnt)
