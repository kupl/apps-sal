n = int(input())
s = [int(i) for i in input().split()]
ans = 1
p = [0] * 100002
for i in s:
    p[i] += 1
for i in range(2, 100002):
    c = 0
    for j in range(i, 100002, i):
        c += p[j]
    ans = max(ans, c)
print(ans)
