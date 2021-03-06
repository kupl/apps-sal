import sys
input = sys.stdin.readline


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


def LI():
    return list(map(int, input().split()))


'\n結局のところ，袋から出し終えた時点で勝敗はついている．\n袋から出す段階でもgrundyの議論ができそう\nあー，でもgが非0のところからg=0に遷移できるとは限らないね．\n\nNが奇数なら\n先手:g=0を目指す\n後手:g≠0を目指す\n\nNが偶数なら\n先手:g≠0を目指す\n後手:g=0を目指す\n\n非0を目指す方が楽そう．最後の方で適当にやれば良いし，\n自分の手番では大きいものからとっていき一箇所にまとめて行く．これで半分以上を取れるので，ちょうど半々になった時のみg=0\nなので，g=0が作れるケースを考える．\n\nNの偶奇や先手/後手にかかわらず，最後の袋を使ってg=0を目指す．\nこれ，できる？\n1手分だけ遡って考える．x0,x1,,,xk 個並んでいるとして，袋は2個残っている．\nこの状態でどんな手を打っても次の手でg=0にされる，という状況はある？\n→ g=0で，かつ，残りの袋がどちらも同じ個数の時はそうか．\nN=偶数で，Aiが全部同じなら後手がg=0を作れるね．\n\n補題:互いに最善手で，g≠0の時に，相手→自分の順でg=0を作れることがあるか?\n→不可かな...微妙．\n\n上で書いたケース以外ないかも?\n全然詰められてないので嘘臭いが投げてみるか...\n→WA\n\n詰めよう．\n\nN=奇数なら後手必勝ぽい？\n後手の行動:大きい袋からとっていき，初手でおかれた皿に置き続ける\n詳細:これをやられたら絶対に過半数を超える．過半数を超えられたくないので先手の人も大きい順位取るけど，それでもAの奇数番目が全て同じ皿に入ってしまう．A1を除いた分でさえ，偶数番目の総和以上になるので，A1も入れると絶対過半数を超える\n\nN=偶数で，後手がg=0を作れるケースを考えようか．\n奇数の時と同じ様に考えられそう?先手側はとにかく大きいのからとっていき一箇所にまとめる．\n→2個セットになっているか，でg=0が作れるか判定できそう\n\n\n'


def main():
    mod = 10 ** 9 + 7
    T = I()
    for _ in range(T):
        N = I()
        A = LI()
        if N % 2 == 1:
            print('Second')
        else:
            flag = 1
            from collections import defaultdict
            dd = defaultdict(int)
            for i in range(N):
                dd[A[i]] += 1
            for (k, v) in list(dd.items()):
                if v % 2:
                    flag = 0
                    break
            if flag == 1:
                print('Second')
            else:
                print('First')


main()
