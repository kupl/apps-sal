#   Battle

class Monster:
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack
        self.death = False


class Game:
    def __init__(self, monsters: list):
        self.monsters = monsters

    def calc_damage(self, offence, defence):
        self.monsters[defence].hp -= self.monsters[offence].attack
        if self.monsters[defence].hp <= 0:
            self.monsters[defence].death = True
        return self.monsters[defence].death

    def battle(self):
        while True:
            self.calc_damage(0, 1)
            if self.monsters[1].death:
                print("Yes")
                break
            self.calc_damage(1, 0)
            if self.monsters[0].death:
                print("No")
                break


a, b, c, d = list(map(int, input().split()))

t_monster = Monster(a, b)
a_monster = Monster(c, d)

game = Game([t_monster, a_monster])
game.battle()

