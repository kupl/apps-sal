a, b, k = map(int, input().split())
ans = set([])
for i in range(a, min(a + k, b)):
    ans.add(i)
for i in range(max(b - k + 1, a), b + 1):
    ans.add(i)
ans = list(ans)
ans.sort()
for i in ans:
    print(i)
