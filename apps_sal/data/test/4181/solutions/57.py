n = int(input())
monster_list = list(map(int, input().split()))
kill_mon = list(map(int, input().split()))

# 配列数を合わせる
kill_mon.append(0)

# 持ち越しパワーの初期化
killed_monster = 0
carry_power = 0
for mons, kill in zip(monster_list, kill_mon):   
    # 全パワーを使い果たす
    if mons >= (kill + carry_power):
        killed_monster += (kill + carry_power)
        # 持ち越しパワーの初期化
        carry_power = 0
    # 余力を残して勝利する
    else:
        killed_monster += mons
        # 前回余力は今回のモンスターにしか使えない。次回のバトルに持ち越せない
        # だから、mons - carry_powerとなる
        # ただ、前回余力が今回モンスターよりも多い場合も考慮するためmax関数を使いマイナス値になることを避ける
        # 前回余力だけで今回バトルに勝利したら、今回パワーをそのまま持ち越せる
        carry_power = kill - max(0, mons - carry_power)
print(killed_monster)
