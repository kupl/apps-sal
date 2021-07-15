A, B, C, D = map(int,input().split())

class Monster:
    def __init__(self,life,power):
        self.life = life
        self.power = power

takahasi = Monster(A,B)
aoki = Monster(C,D)

while takahasi.life > 0 and aoki.life > 0:
    AHP = aoki.life - takahasi.power
    aoki.life = AHP
    THP = takahasi.life - aoki.power
    takahasi.life = THP
    if AHP <= 0:
        print("Yes")
        break
    if THP <= 0:
        print("No")
        break
