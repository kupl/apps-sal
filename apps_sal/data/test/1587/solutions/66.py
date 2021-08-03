n = int(input())
c = input()

r_cnt = c.count('R')
w_cnt = c.count('W')

last_c = 'R' * r_cnt + 'W' * w_cnt

num = 0
for i in range(n):
    if c[i] != last_c[i]:
        num += 1

print((num + 2 - 1) // 2)
