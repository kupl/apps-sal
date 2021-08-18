import sys
input = sys.stdin.readline


def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))


"""
各Aiについて「その数を選ばないで，何回の行動ができますか」がわかればいけるかも?
いや，なんか違いそう．

メモ:一応，小さいものがいいわけではない，K=1,Q=2で1,10,100,101とかなら後ろ二つを取りたい

強制的に使う必要があるものがある場合，それ付近で考える?うーん
入力例2とかを見ると「強制で取らないといけないものがない場合は自由に取れる」みたいに見えるけど，部分的にお此れを撮る前にアレを取らなきゃみたいな前提条件みたいなのは出てくる

順番があるので有向グラフを作るか．
入力例1では，1を取らないと2,3は取れないので1から2,3に辺を貼る
グラフができてもどうするんだこれ，i番目から始めた場合jまでいく必要がある，みたいなのを求めていくか-,
N<=2000ならそれでいける?
これ，最小費用流で解けるかも?
s→all→tをつける．頂点間はcap1，コストが差の値で辺を．
いや，これ入力例3みたいなパターンに弱そう．

そもそも有向グラフをどう作るか．
区間DPぽくいけるか?1つ消した後にK個見て最小を探す，というのはK+1個見て下から2番目を探すのと同じよな
泥沼な気がする．一旦リセット

i番目から始めた場合にどこまでいくか，みたいな発想は良さそう．
Xを決め打てばYを最大化する問題
Yを決め打てばXを最小化する問題
Yを決め打てば，Y未満は選べなくなるのでいけそう．

使えないと数字が出てくるので，いくつかの区間に分かれる．逆にその区間ないは全て使える．
いや，全てじゃないや．上位(K-1)個以外は全部使える．
Xを最小化したいので，使える数字をしたから選んでいく

"""


def main():
    mod = 10**9 + 7
    N, K, Q = MI()
    A = LI()
    inf = 10**10

    if Q == 1:
        print((0))
        return()

    def calc(Y):
        L = []
        temp = []
        for a in A:
            if a >= Y:
                temp.append(a)
            else:
                if len(temp) >= K:
                    temp.sort()
                    if K > 1:
                        L += temp[:-(K - 1)]
                    else:
                        L += temp

                temp = []

        if len(temp) >= K:
            temp.sort()
            if K > 1:
                L += temp[:-(K - 1)]
            else:
                L += temp
        L.sort()

        if len(L) >= Q:
            return L[Q - 1]
        else:
            return inf

    ans = inf

    for b in A:
        y = b
        x = calc(y)
        temp = x - y
        ans = min(ans, temp)

    print(ans)


main()
