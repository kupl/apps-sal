A, B, C, D = map(int,input().split())

class Monster:
    def __init__(self, life, power):
        self.life = life
        self.power = power

def answer(A: int, B: int, C: int, D: int) -> str:
    takahasi = Monster(A, B)
    aoki = Monster(C, D)

    while takahasi.life > 0 and aoki.life > 0:
        A_HP = aoki.life - takahasi.power
        aoki.life = A_HP
        T_HP = takahasi.life - aoki.power
        takahasi.life = T_HP
        if A_HP <= 0:
            return "Yes"
            break
        if T_HP <= 0:
            return "No"
            break

print(answer(A, B, C, D))
