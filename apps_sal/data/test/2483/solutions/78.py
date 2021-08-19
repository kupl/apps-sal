# https://atcoder.jp/contests/abc080/tasks/abc080_d
# D - Recording

N, C = list(map(int, input().split()))
s = [0] * N
t = [0] * N
c = [0] * N
f = [False] * C
yoyaku = [False] * C
L = []
for i in range(N):
    s[i], t[i], c[i] = list(map(int, input().split()))
    L.append([s[i] - 0.5, c[i] - 1, 1])
    L.append([t[i], c[i] - 1, 0])

L.sort()
# print(L)
ans = 0
tmp = 0

for i, (time, ch, sw) in enumerate(L):
    if sw == 1:
        if f[ch] == False:
            tmp += 1
            f[ch] = True
            ans = max(ans, tmp)
        else:
            yoyaku[ch] = True
    else:
        if yoyaku[ch]:
            yoyaku[ch] = False
        else:
            tmp -= 1
            f[ch] = False

print(ans)
