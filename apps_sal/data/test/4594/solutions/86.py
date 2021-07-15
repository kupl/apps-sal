n = int(input())
d = list()
ans = 0
for i in range(n):
    d.append(int(input()))
    if d[i] not in d[:i]:
        ans += 1

print(ans)
