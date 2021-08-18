N = int(input())
A = [int(input()) for _ in range(N)]

c = {}
ans = 0

for i in A:
    if i not in c.keys():
        c[i] = 0
    c[i] += 1

for j in c.values():
    if j % 2 == 1:
        ans += 1

print(ans)
