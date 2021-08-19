class Monster:

    def __init__(self, hp, at):
        self.hp = hp
        self.at = at

    def fight(self, at) -> int:
        self.hp -= at
        return self.hp

    def is_loser(self) -> bool:
        return self.hp <= 0


(A, B, C, D) = map(int, input().split())
takahashi_monster = Monster(A, B)
aoki_monster = Monster(C, D)
while True:
    aoki_monster.fight(B)
    if aoki_monster.is_loser():
        result = 'Yes'
        break
    takahashi_monster.fight(D)
    if takahashi_monster.is_loser():
        result = 'No'
        break
print(result)
