# https://qiita.com/goto_yuta_/items/1c104e332351ab9389a6
# 入力を整数に変換して受け取る
import sys
sys.setrecursionlimit(10 ** 6)  # pypy3はnumpyを使えない，この行を消すこと．
# 入力を整数に変換して受け取る
def II(): return int(sys.stdin.readline())
# 入力全てを整数に変換したものの配列を受け取る
def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力の文字列を1文字ずつに分けたものの配列を受け取る
def LC(): return list(input())
# 入力の数字列を1桁ずつに分けたものの配列を受け取る
def IC(): return [int(c) for c in input()]
# 少ない1行のint変数に入れる様の入力．例:N, A, B = map(int, input().split())
def MI(): return map(int, input().split())


X, Y = MI()
Out = 1
while(X * 2 <= Y):
    Out += 1
    X *= 2
print(Out)
