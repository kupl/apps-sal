n, m = map(int, input().split())
s = input()
n += 1

pos = [n - 1]
ind = n - 1
while True:
    tmp = -1
    for i in range(1, m + 1):
        if s[max(ind - i, 0)] == "0":
            tmp = max(ind - i, 0)
    if tmp == -1:
        print(-1)
        return
    pos.append(tmp)
    ind = tmp
    if ind == 0:
        break
tmp = pos[::-1]
ans = []
for i in range(len(tmp) - 1):
    ans.append(tmp[i + 1] - tmp[i])
print(*ans)
