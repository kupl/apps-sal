n = int(input())
a = [int(x) for x in input().split()]
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
ans = -1
for i in d:
    ans = max(ans, d[i])
print(ans)
