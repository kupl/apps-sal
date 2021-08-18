class Monster:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def fight(self, power) -> int:
        self.hp -= power
        return self.hp

    def is_loser(self) -> bool:
        return self.hp <= 0


a, b, c, d = map(int, input().split())

takahashi_monster = Monster(a, b)
aoki_monster = Monster(c, d)
result = "ret"

while True:
    aoki_monster.fight(b)
    if aoki_monster.is_loser():
        result = "Yes"
        break
    else:
        pass

    takahashi_monster.fight(d)
    if takahashi_monster.is_loser():
        result = "No"
        break
    else:
        pass

print(result)
