(a, b, k) = map(int, input().split())
if b - a < k:
    k = b - a
if k == 0:
    k = 1
ans = []
for i in range(a, a + k):
    ans.append(i)
for j in range(b, b - k, -1):
    ans.append(j)
ans = sorted(set(ans))
for i in ans:
    print(i)
