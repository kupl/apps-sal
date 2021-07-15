H, n = (int(t) for t in input().split(' '))
d = [int(t) for t in input().split(' ')]

hp_diff = sum(d)

current_hp = 0
rip_hp_max = 0
for di in d:
    current_hp += di
    rip_hp_max = max(rip_hp_max, -current_hp)

if hp_diff < 0 and rip_hp_max < H:
    required_full_rounds = (H - rip_hp_max) // -hp_diff
else:
    required_full_rounds = 0

hp_after_full_rounds = H + required_full_rounds * hp_diff
current_hp = hp_after_full_rounds
for i in range(2*n):
    current_hp += d[i % n]
    if current_hp <= 0:
        print(i+1+required_full_rounds*n)
        return

print(-1)

