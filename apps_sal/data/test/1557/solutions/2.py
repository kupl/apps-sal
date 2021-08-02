my_health, my_attack, my_potion = [int(x) for x in input().split()]
boss_health, boss_attack = [int(x) for x in input().split()]

actions = []

while boss_health > 0:
    if my_health <= boss_attack and boss_health > my_attack:
        actions.append('HEAL')
        my_health += my_potion
    else:
        actions.append('STRIKE')
        boss_health -= my_attack
        if boss_health <= 0:
            break
    my_health -= boss_attack

print(len(actions))
print('\n'.join(actions))
