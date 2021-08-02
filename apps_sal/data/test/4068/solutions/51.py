n, m = map(int, input().split())
ans = [0] * (n + 1)
ans[0] = 1
p = 10 ** 9 + 7
for i in range(m):
    ans[int(input())] = -1

if ans[1] != -1:
    ans[1] = 1

for i in range(2, n + 1):
    if ans[i] == -1:
        continue
    ans[i] = max(ans[i - 1], 0) + max(ans[i - 2], 0)
    ans[i] %= p
print(ans[n])
