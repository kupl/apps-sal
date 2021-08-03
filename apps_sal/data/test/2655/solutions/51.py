N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ans = 0

i = 0  # 何人目のフレンドリーさがプラスされるか
nokori = N - 1  # 残り入れなければならない人数
while nokori > 0:
    if i == 0:  # 最もフレンドリーな人は初めに入れる
        ans += A[i]
        nokori -= 1
    else:
        if nokori == 1:
            ans += A[i]
            nokori -= 1
        else:
            ans += 2 * A[i]
            nokori -= 2
    i += 1

print(ans)
