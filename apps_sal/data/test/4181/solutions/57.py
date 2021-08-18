n = int(input())
monster_list = list(map(int, input().split()))
kill_mon = list(map(int, input().split()))

kill_mon.append(0)

killed_monster = 0
carry_power = 0
for mons, kill in zip(monster_list, kill_mon):
    if mons >= (kill + carry_power):
        killed_monster += (kill + carry_power)
        carry_power = 0
    else:
        killed_monster += mons
        carry_power = kill - max(0, mons - carry_power)
print(killed_monster)
