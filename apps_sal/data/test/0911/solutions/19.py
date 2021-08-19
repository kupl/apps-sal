(n, c) = list(map(int, input().split()))
p = list(map(int, input().split()))
t = list(map(int, input().split()))
sum_l = 0
sum_r = 0
t_l = 0
t_r = 0
for i in range(n):
    t_l += t[i]
    sum_l += max(0, p[i] - t_l * c)
p.reverse()
t.reverse()
for i in range(n):
    t_r += t[i]
    sum_r += max(0, p[i] - t_r * c)
if sum_l > sum_r:
    print('Limak')
elif sum_l < sum_r:
    print('Radewoosh')
else:
    print('Tie')
