#https://blacktanktop.hatenablog.com/entry/2020/08/05/073335 をまねした
n = int(input())
C = input()
r_all = C.count('R')
# CをRWRWRWRとした時に、
# どの状態にするのが最小手数かがわからないので全パターンである以下の状態における最小手数を計算する。
# ある場所を境に右側をW左側をRとするイメージ。
# |RWRWRWR→WWWWWWW
# R|WRWRWR→RWWWWWW
# RW|RWRWR→RRWWWWW
# .......
# RWRWRW|R→RRRRRRW
# RWRWRWR|→RRRRRRR
# 最小手数をリストに入れておく。パターンはn+1
move = [0] * (n+1)
# 実際の並びにおいて、|の左のW右のRの数をw, rとする
# 初期値はw=0, r=CのうちRの数
w = 0
r = r_all
# moveの初期値はすべてWを目指すので
move[0] = max(0, r_all)
# forで１文字ずつ見ていくのは区切りを一つずつずらしているイメージ
# Cの文字をみてWならwを1増やしてRならrを1減らす
# （区切りの左のWの数がwで右のRの数がrなので）
for idx, c in enumerate(C):
    if c == 'W':
        w += 1
    else:
        r -= 1 
    move[idx+1] = max(w, r)
ans = min(move)
print(ans) 
