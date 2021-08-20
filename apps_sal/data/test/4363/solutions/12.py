def main():
    (stdIn1, stdIn2) = list(map(int, input().split()))
    stdOut = solve(stdIn1, stdIn2)
    print(stdOut)


'\n方針\nx,y,zそれぞれを3重ループで0からkまで回す\n(O(N^3)だが、k<=2500なので気にならない)\nx+y+zが等しければパターンを1追加\n\nTLEになったので、もう少し節約するパターンを考える必要あり\nひとまずx,x+y,x+y+zがsより大きなった場合はbreakさせてループを抜ける処理にしてみる\nまだTLEになるので、もう少し考える\n実はzはループする必要はなく z = s - (x + y) <= k であれば +1, > k であれば continueでよい\nこれでO(N^2)に計算量を抑えられる\n\n'


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
