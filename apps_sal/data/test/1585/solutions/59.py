#atcoder template
def main():
    import sys
    input = sys.stdin.readline
    #文字列入力の時は上記はerrorとなる。
    #ここにコード
    #input
    x, y = map(int, input().split())

    #output
    #y以下でも最も大きい2^z

    answer = 0
    if x == 1:
        answer = 1
        while pow(2, answer) <= y:
            answer += 1
    else:
        while x * pow(2, answer) <= y:
            answer += 1

    print(answer)

    #N = 1のときなどcorner caseを確認！
def __starting_point():
    main()
__starting_point()
