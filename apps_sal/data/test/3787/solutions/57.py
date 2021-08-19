import sys
input = sys.stdin.readline


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


def LI():
    return list(map(int, input().split()))


'\n和はN+1以下である．\nA列とB列の両方で共通して持てるのは1個までなので．\n下限はどれくらいだろう．\n\nA=1 or B=1なら相方はN確定．\n基本的にAもBも1ではない前提で話す\n\nとりあえず構築を考えるか．\nA+B=N+1なら簡単．\nB,B-1,...,2,1,B+1,B+2,...N\nで良い．手前にB列，奥にA列を固める．\n\nA+B=N-1でない場合，A列に使うものとB列に使うものはかぶらなくて良い．\n手前に大きい順にB個だけ並べておけば，\nN-B個の順列で\nLIS=Aかつ\nLDS≠B\nを満たせるか，という問題に帰着．\nうーん，\n\nこのやり方でN=20，A=2,B=5にできる?無理，1からみてLISを3にならないようにするには降順に並べるしかない\nいくつかのグループに分けようか．\n17~20, 13~16, 9~12, 5~8, 1~4\nのグループに分けて，グループ内では昇順にすれば\nA=4,B=5まではいける．B=5を固定したらこれがAの最小な気がする\nAの最小値はN/Bの切り上げ，かな\n'


def main():
    mod = 10 ** 9 + 7
    (N, A, B) = MI()
    if A + B > N + 1:
        print(-1)
        return
    t = (N + B - 1) // B
    if A < t:
        print(-1)
        return
    if A == 1:
        if B == N:
            ans = list(range(N, 0, -1))
            print(' '.join(map(str, ans)))
            return
        else:
            print(-1)
            return
    if B == 1:
        if A == N:
            ans = list(range(1, N + 1))
            print(' '.join(map(str, ans)))
            return
        else:
            print(-1)
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
    print(' '.join(map(str, ans)))


main()
