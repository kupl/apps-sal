(n, m) = map(int, input().split())
s = [input().split() for i in range(n)]
ans = 0
for i in range(n):
    cur_r = s[i]
    prev_1 = 0
    prev_0 = 0
    for j in cur_r:
        if j == '1':
            ans += prev_0
            prev_0 = 0
            prev_1 = 1
        else:
            ans += prev_1
            prev_0 += 1
for i in range(m):
    prev_1 = 0
    prev_0 = 0
    for t in range(n):
        j = s[t][i]
        if j == '1':
            ans += prev_0
            prev_0 = 0
            prev_1 = 1
        else:
            ans += prev_1
            prev_0 += 1
print(ans)
