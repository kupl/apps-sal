# 深さ優先探索による迷路の最短距離計算


import numpy as np
import sys
import copy
import queue

# 再帰上限
sys.setrecursionlimit(10 ** 6)


# 最短距離メモ
# 0#4#
# 123
# 23#のような最終結果のためのメモ
# スタートからの最短距離が格納

def answer_sheet(meiro):
    return copy.deepcopy(meiro)


# 【周りの点の取得）
# 座標が与えられると、上下左右の4点を得る。
# 境界を超えた場合はカットされる。
def get_around_point(point, h, w):
    around_points = []

    for ij in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        i, j = ij
        new_i = point[0] + i
        new_j = point[1] + j
        if 0 <= new_i < h and 0 <= new_j < w:
            around_points.append([new_i, new_j])
    return around_points


# ある点が道かどうかを判別する
def walkable(point, meiro):
    i = point[0]
    j = point[1]
    if meiro[i][j] == ".":
        return True
    return False


# ある点が行ったことあるかどうか
def never_had_been(point, sheet):
    if sheet[point[0]][point[1]] == ".":
        return True
    else:
        return False


# キューに、ある点の周りの行ったことのない道を追加し、シートに距離を記入
def add_load_2_queue(point, h, w, meiro, sheet, que):
    around_points = get_around_point(point, h, w)
    for around_point in around_points:
        if walkable(around_point, meiro) and never_had_been(around_point, sheet):
            que.put(around_point)
            sheet[around_point[0]][around_point[1]] = sheet[point[0]][point[1]] + 1
    return sheet, que


# ポイントが与えられたとき、その周りの道をキューに追加し、シートに記入、次のキューを取り出し同様の処理を行う。キューがなくなるまで続け、シートを返す。
def step(point, h, w, meiro, sheet, que):
    sheet, que = add_load_2_queue(point, h, w, meiro, sheet, que)
    if que.empty():
        return sheet
    next_point = que.get()
    return step(next_point, h, w, meiro, sheet, que)


# シートは、行けない場所の場合は"#"が含まれているため-1に変換
def hash2minus(sheet):
    new_sheet = []
    for gyou in sheet:
        new_gyou = []
        for item in gyou:
            if item == "#":
                new_gyou.append(-1)
            else:
                new_gyou.append(item)
        new_sheet.append(new_gyou)
    return new_sheet


# -------メイン関数---------
# スタートを決めた場合の、各場所までの最短距離を表すシートを出力
# 行けない場所の場合は-1
# 入力
# start 開始座標のリスト(例：[1,2])
# h 迷路の高さ
# w 迷路の幅
# meiro 迷路の文字列リスト
def min_dis(start, h, w, meiro):
    sheet = answer_sheet(meiro)
    que = queue.Queue()
    sheet[start[0]][start[1]] = 0
    return hash2minus(step(start, h, w, meiro, sheet, que))


h, w = [int(i) for i in input().split()]
meiro = []

for i in range(h):
    meiro.append(list(input()))

ans = 0
for i in range(h):
    for j in range(w):
        if meiro[i][j] == ".":
            ans = max(ans, np.max(np.array(min_dis([i, j], h, w, meiro))))

print(ans)
