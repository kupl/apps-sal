import sys
input = sys.stdin.readline


def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))


"""
和はN+1以下である．
A列とB列の両方で共通して持てるのは1個までなので．
下限はどれくらいだろう．

A=1 or B=1なら相方はN確定．
基本的にAもBも1ではない前提で話す

とりあえず構築を考えるか．
A+B=N+1なら簡単．
B,B-1,...,2,1,B+1,B+2,...N
で良い．手前にB列，奥にA列を固める．

A+B=N-1でない場合，A列に使うものとB列に使うものはかぶらなくて良い．
手前に大きい順にB個だけ並べておけば，
N-B個の順列で
LIS=Aかつ
LDS≠B
を満たせるか，という問題に帰着．
うーん，

このやり方でN=20，A=2,B=5にできる?無理，1からみてLISを3にならないようにするには降順に並べるしかない
いくつかのグループに分けようか．
17~20, 13~16, 9~12, 5~8, 1~4
のグループに分けて，グループ内では昇順にすれば
A=4,B=5まではいける．B=5を固定したらこれがAの最小な気がする
Aの最小値はN/Bの切り上げ，かな
"""


def main():
    mod = 10**9 + 7
    N, A, B = MI()

    if A + B > N + 1:
        print((-1))
        return

    t = (N + B - 1) // B
    if A < t:
        print((-1))
        return

    if A == 1:
        if B == N:
            ans = list(range(N, 0, -1))
            print((' '.join(map(str, ans))))
            return
        else:
            print((-1))
            return

    if B == 1:
        if A == N:
            ans = list(range(1, N + 1))
            print((' '.join(map(str, ans))))
            return
        else:
            print((-1))
            return

    ans = []
    temp = list(range(N - A + 1, N + 1))
    ans += temp
    unit = (N - A) // (B - 1)
    rem = (N - A) % (B - 1)

    right = N - A
    for i in range(B - 1):
        left = right - unit
        if rem:
            left -= 1
            rem -= 1
        temp = list(range(left + 1, right + 1, 1))
        ans += temp
        right = left

    print((' '.join(map(str, ans))))


main()
