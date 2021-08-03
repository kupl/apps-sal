# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main():
    enemy_hp = int(input())
    enemy_count = 1
    attack_count = 1

    if enemy_hp == 1:
        print(1)
        return
    else:
        while enemy_hp > 1:
            enemy_hp = int(enemy_hp / 2)
            enemy_count *= 2
            attack_count += enemy_count

    print(attack_count)


def __starting_point():
    main()


__starting_point()
