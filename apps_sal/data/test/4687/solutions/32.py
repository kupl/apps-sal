n, k = map(int, input().split())

q = []
for i in range(n):
    q.append(list(map(int, input().split())))

q = sorted(q, key=lambda x: x[0])
cnt = 0
i = 0
while cnt < k:
    a, b = q[i]
    cnt += b
    i += 1
print(a)
