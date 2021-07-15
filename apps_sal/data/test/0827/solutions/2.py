#https://qiita.com/goto_yuta_/items/1c104e332351ab9389a6
# 入力を整数に変換して受け取る
import sys
sys.setrecursionlimit(10 ** 6)#pypy3はnumpyを使えない，この行を消すこと．
# 入力を整数に変換して受け取る
def II(): return int(sys.stdin.readline())
# 入力全てを整数に変換したものの配列を受け取る
def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力の文字列を1文字ずつに分けたものの配列を受け取る
def LC(): return list(input())
# 入力の数字列を1桁ずつに分けたものの配列を受け取る
def IC():return [int(c) for c in input()]
#少ない1行のint変数に入れる様の入力．例:N, A, B = map(int, input().split())
def MI(): return map(int, input().split())
def solve():
    N = II()
    T = input()
    if(N==1):
        if(T=='0'):
            print(10000000000)
            return
        elif(T=='1'):
            print(20000000000)
            return
    elif(N==2):
        if(T=='11' or T =='10'):
            print(10000000000)
            return
        elif(T=='01'):
            print(9999999999)
            return
        else:
            print(0)
            return
    else:
        First = T[:3]
        if(First != "110" and First != "101" and First != "011"):
            print(0)
            return
        for i in range(3,N-2,3):#途中までの確認
            if(First != T[i:i+3]):
                print(0)
                return
        #末尾の処理
        if(N%3 == 1):
            if(First[0] != T[-1]):#最初の1文字と末尾の1文字の一致
                print(0)
                return
        elif(N%3 == 2):
            if(First[0:2] != T[-2:]):#最初の2文字と末尾の2文字の一致
                print(0)
                return
        from math import ceil, floor
        if(First == "110"):
            print(10000000000-floor((N-1)/3))
            return
        elif(First == "101" or First == "011"):
            print(9999999999 - floor((N-2) / 3))
            return
    return
solve()
