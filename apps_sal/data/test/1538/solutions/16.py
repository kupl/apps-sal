n = int(input())
a = list(map(int, input().split()))

a = sorted(a, key=lambda x: -x)
ans = 0
d = {}
for i in a:
    if i not in d:
        d[i] = 0
    d[i] += 1
for key in d:
    ans = max(ans, d[key])
print(ans)
