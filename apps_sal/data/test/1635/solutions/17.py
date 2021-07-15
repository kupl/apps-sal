n = int(input())
l = list(map(int, input().split()))
s = set()
ans = -1
for i in range(n - 1, -1, -1):
    if l[i] not in s:
        s.add(l[i])
        ans = l[i]
print(ans)

