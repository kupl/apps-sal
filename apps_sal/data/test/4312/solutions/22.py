(t_hp, t_atk, a_hp, a_atk) = list(map(int, input().split()))
t_count = 0
a_count = 0
while a_hp > 0:
    a_hp -= t_atk
    t_count += 1
while t_hp > 0:
    t_hp -= a_atk
    a_count += 1
if t_count <= a_count:
    print('Yes')
else:
    print('No')
