n, m, k = map(int, input().split())
sila = list(map(int, input().split()))
uch = list(map(lambda x: int(x) - 1, input().split()))
maxses = [0 for i in range(m)]
for i in range(n):
    maxses[uch[i]] = max(maxses[uch[i]], sila[i])
c = list(map(lambda x: int(x) - 1, input().split()))
ans = 0
for i in c:
    if sila[i] < maxses[uch[i]]:
        ans += 1
print(ans)
