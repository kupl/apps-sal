def mp():
    return map(int, input().split())


n = int(input())
a = list(mp())
a = a[:] + a[:]
cnt = 0
ans = cnt
for i in range(2 * n):
    if a[i] == 0:
        ans = max(ans, cnt)
        cnt = 0
    else:
        cnt += 1
ans = max(ans, cnt)
print(ans)
