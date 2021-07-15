n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append([a[i], i])
b.sort(key=lambda x: x[0], reverse=True)
cnt = 0
s = 0
res = []
for i in range(n):
    s += cnt * b[i][0] + 1
    cnt += 1
    res.append(str(b[i][1] + 1))
print(s)
print(' '.join(res))

