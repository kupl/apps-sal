N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
ans = pos = 0
flag = [0] * N
while True:
    ans += 1
    if a[pos] == 2:
        break
    pos = a[pos] - 1
    if flag[pos] > 0:
        ans = -1
        break
    else:
        flag[pos] = 1
print(ans)
