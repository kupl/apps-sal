n = int(input())
data = list(map(int, input().split()))
d = [False] * (n + 4)
d[0] = True
res = 1
for i in range(n):
    if d[data[i]]:
        d[data[i]] = False
        d[i + 1] = True
    else:
        d[i + 1] = True
        res += 1
print(res)
