n = int(input())
c = str(input())
ans = 0

r_cnt = c.count('R')

for i in range(r_cnt):
    if c[i] == 'W':
        ans += 1

print(ans)
