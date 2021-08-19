import sys
n = int(input())
type = input().split()
fa = list(map(int, input().split()))
degree = [0] * (n + 1)
for i in fa:
    degree[i] += 1
type = [0] + type
fa = [0] + fa
max = 0
maxi = 0
for i in range(1, n + 1):
    if type[i] == '1':
        cnt = 0
        cur = fa[i]
        while not (cur == 0 or type[cur] == '1' or degree[cur] > 1):
            cnt += 1
            cur = fa[cur]
        if max <= cnt:
            max = cnt
            maxi = i
print(max + 1)
ans = []
cur = maxi
while not (not cur or (type[cur] == '1' and cur != maxi) or degree[cur] > 1):
    ans.append(cur)
    cur = fa[cur]
print(*ans[::-1])
