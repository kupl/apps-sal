a, b, k = map(int, input().split())
ans = []
for i in range(k):
    if a <= a + i <= b:
        ans.append(a + i)
    if a <= b - i <= b:
        ans.append(b - i)
ans = list(set(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])
