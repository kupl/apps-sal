H = int(input())


def attack_num(x):
    if x == 1:
        return 1
    else:
        return 2 * attack_num(x // 2) + 1


print(attack_num(H))
