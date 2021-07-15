def judge():
    cnt = 0  # 今何連続でゾロ目が出ているか記録しておきます

    for _ in range(N):
        x, y = map(int, input().split())
        if x == y:
            # ゾロ目ストリークが1増えました
            cnt += 1
        else:
            # ゾロ目ストリークが切れました
            cnt = 0

        if cnt == 3:
            # 3連続になった瞬間、return True していいです
            return True

    # ダメでした
    return False

N = int(input())

if judge():
    # judge() で Trueが返ってくるとこっちに進みます
    print("Yes")
else:
    # Falseだとこっちです
    print("No")
