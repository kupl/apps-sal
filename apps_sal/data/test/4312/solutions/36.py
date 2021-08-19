class Monster:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def fight(self, power) -> int:
        self.hp -= power
        return self.hp

    def is_loser(self) -> bool:
        return self.hp <= 0


# 標準入力から A, B, C, D を取得する
a, b, c, d = map(int, input().split())

takahashi_monster = Monster(a, b)   # 高橋モンスター
aoki_monster = Monster(c, d)    # 青木モンスター
result = "ret"

while True:
    aoki_monster.fight(b)   # 高橋の攻撃
    if aoki_monster.is_loser():
        result = "Yes"
        break
    else:
        pass

    takahashi_monster.fight(d)  # 青木の攻撃
    if takahashi_monster.is_loser():
        result = "No"
        break
    else:
        pass

print(result)
