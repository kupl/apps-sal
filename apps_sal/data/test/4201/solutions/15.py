h, w, k = map(int, input().split())
ans = [list(input()) for i in range(h)]
n = h + w
answer = 0
for i in range(1 << n):
    cond = [0] * n
    for j in range(n):
        if 1 & (i >> j):
            cond[j] = 1
    count = 0
    for i in range(h):
        for j in range(w):
            if cond[i] == 0 and cond[h + j] == 0 and ans[i][j] == "
            count += 1
    if count == k:
        answer += 1
print(answer)
