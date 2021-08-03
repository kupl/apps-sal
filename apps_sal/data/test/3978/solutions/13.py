n = int(input())
l = sorted(map(int, input().split()))
seen = [False] * n
res = 0
for i in range(n):
    if seen[i]:
        continue
    res += 1
    for j in range(i, n):
        seen[j] |= l[j] % l[i] == 0
print(res)
