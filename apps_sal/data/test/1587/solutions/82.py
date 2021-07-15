n = int(input())
ccc = input()
cnt_r = ccc.count('R')
ans = 0
for i in range(cnt_r):
    if ccc[i] == 'W':
        ans += 1
print(ans)
