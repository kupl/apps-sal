(N, C) = map(int, input().split())
ch = [[0] * (10 ** 5 + 1) for _ in range(C)]
for _ in range(N):
    (s, t, c) = map(int, input().split())
    ch[c - 1][s] += 1
    ch[c - 1][t] -= 1
for c in range(C):
    for i in range(10 ** 5):
        if ch[c][i + 1] == 1:
            ch[c][i + 1] = ch[c][i + 1] + ch[c][i]
            ch[c][i] = 1
        else:
            ch[c][i + 1] = ch[c][i + 1] + ch[c][i]
ans = 0
for i in range(10 ** 5):
    temp = 0
    for c in range(C):
        temp += ch[c][i + 1]
    ans = max(ans, temp)
print(ans)
