
def main():
    stdIn1, stdIn2 = list(map(int, input().split()))
    stdOut = solve(stdIn1, stdIn2)
    print(stdOut)


"""
方針
x,y,zそれぞれを3重ループで0からkまで回す
(O(N^3)だが、k<=2500なので気にならない)
x+y+zが等しければパターンを1追加

TLEになったので、もう少し節約するパターンを考える必要あり
ひとまずx,x+y,x+y+zがsより大きなった場合はbreakさせてループを抜ける処理にしてみる
まだTLEになるので、もう少し考える
実はzはループする必要はなく z = s - (x + y) <= k であれば +1, > k であれば continueでよい
これでO(N^2)に計算量を抑えられる

"""


def solve(k, s):
    pattern = 0
    for x in range(k + 1):
        if x > s:
            break
        for y in range(k + 1):
            if x + y > s:
                break
            z = s - x - y
            if z <= k:
                pattern += 1

    return pattern


def __starting_point():
    main()


__starting_point()
