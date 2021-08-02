# モンスターのデータ
class Monster:
    def __init__(self, hp, at):
        self.hp = hp
        self.at = at

# 「戦闘」を定義。値の推移
    def fight(self, at) -> int:
        self.hp -= at
        return self.hp
# hpからatを引く。その値を再びhpに返す

# 「敗北」を定義する
    def is_loser(self) -> bool:
        return self.hp <= 0


A, B, C, D = map(int, input().split())

takahashi_monster = Monster(A, B)
aoki_monster = Monster(C, D)


while True:
    aoki_monster.fight(B)  # 高橋の攻撃
    if aoki_monster.is_loser():
        result = 'Yes'
        break

    takahashi_monster.fight(D)  # 青木の攻撃
    if takahashi_monster.is_loser():
        result = 'No'
        break

print(result)
