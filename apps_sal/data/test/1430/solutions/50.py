
def resolve():
    N, K = map(int, input().split())
    S = input()

    # even:1
    # odd:0
    # 1-0-1-0-1 の配列にする. 両端は1にする
    L = []
    pre = "1"
    cnt = 0
    for i in range(N):
        if pre == S[i]:
            cnt += 1
        else:
            L.append(cnt)
            cnt = 1
        pre = S[i]
    L.append(cnt)
    # 最後が0で終わっていたら、仮の1を付け足す。(値が0なので影響ない)
    if pre == "0":
        L.append(0)

    # 1-0-1-0-1の配列を作成し、K＝2だとする。
    # 0を2個含めた個数は, 1＝3、0＝2の長さが作成できる
    length = 2 * K + 1

    # 0をすべて変換できる
    if len(L) <= length:
        return print(N)

    # 1-0-1-0-1の配列なので間に0を含んだ数え上げ
    # なので偶数とびに1を起点に数え上げ
    left = 0
    right = 0
    tmp = 0
    # しゃくとり
    ans = 0
    for i in range(0, len(L), 2):
        nextL = i
        nextR = min(i + length, len(L))

        while nextL > left:
            tmp -= L[left]
            left += 1
        while nextR > right:
            tmp += L[right]
            right += 1

        ans = max(ans, tmp)
        
    print(ans)


def __starting_point():
    resolve()
__starting_point()
