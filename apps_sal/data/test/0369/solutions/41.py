n, m = map(int, input().split())
s = input()
out_s = '1' * (m)
if out_s in s:
    print(-1)
    return
s = s[::-1]
if s[0] == "1":
    print(-1)
    return
pre = [-1] * (n + 1)
stack = [0]
while stack:
    now = stack.pop()
    if now == n:
        break
    for i in range(1, m + 1):
        tsugi = now + i
        if tsugi > n:
            continue
        if s[tsugi] == "1":
            continue
        pre[tsugi] = now
        stack.append(tsugi)
else:
    print(-1)
    return
ato = n
mae = pre[n]
ans = []
while mae >= 0:
    ans.append(ato - mae)
    ato = mae
    mae = pre[ato]
print(*ans, sep=" ")
