R = lambda: map(int, input().split())
n, k = R()
arr = list(R())
q, tq = [arr], []
while k:
    cur = q.pop(0)
    for i in range(n):
        for j in range(i + 1):
            tq.append(cur[:j] + cur[j:i + 1][::-1] + cur[i + 1:])
    if not q:
        q, tq = tq, []
        k -= 1
res = 0
for ar in q:
    cnt = 0
    for i in range(n):
        for j in range(i):
            cnt += ar[j] > ar[i]
    res += cnt / len(q)
print(res)
