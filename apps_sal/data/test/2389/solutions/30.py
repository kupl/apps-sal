def main():
    N, A, B, C = list(map(int, input().split()))
    d = {'AB': (0, 1), 'AC': (0, 2), 'BC': (1, 2)}
    s = [d[input()] for _ in range(N)]
    abc = [A, B, C]
    ABC = 'ABC'
    ans = []
    for i in range(N):
        x, y = s[i]
        # 強制終了
        if abc[x] == abc[y] == 0:
            print('No')
            return
        if abc[x] == abc[y] == 1:
            # 最後の要素 or 次に今回選ぶ可能性があるものがあるかどうか
            if (i == N - 1) or (x in s[i + 1]):
                ans.append(ABC[x])
                abc[x] += 1
                abc[y] -= 1
            else:
                ans.append(ABC[y])
                abc[x] -= 1
                abc[y] += 1
        # 2数の和が1 or 3以上の場合は大きい方をインクリメント, 小さい方をデクリメントする.
        # 2数が同じ場合には 後半の文字に対応する番号を優先する.
        else:
            if abc[x] > abc[y]:
                ans.append(ABC[y])
                abc[x] -= 1
                abc[y] += 1
            else:
                ans.append(ABC[x])
                abc[x] += 1
                abc[y] -= 1
    print('Yes')
    for a in ans:
        print(a)


main()
