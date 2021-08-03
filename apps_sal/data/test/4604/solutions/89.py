n = int(input())
a = sorted(list(map(int, input().split())))

if n % 2 == 0:  # 人数が偶数の場合に不整合があるか確認
    for i in range(0, n, 2):
        if a[i] != i + 1 or a[i] != a[i + 1]:
            print(0)
            return
else:  # 人数が奇数の場合に不整合があるか確認
    if a[0] != 0:  # 差分が0存在していることを確認
        print(0)
        return
    else:
        for i in range(1, n, 2):
            if a[i] != i + 1 or a[i] != a[i + 1]:
                print(0)
                return

ans = 1
for i in range(n // 2):
    ans = ans * 2 % (10**9 + 7)  # 組み合わせとしては同じ差分の値を入れ替える2択になるので、結果を2倍にする
print(ans)
