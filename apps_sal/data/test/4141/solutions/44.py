# 書類に書かれている整数のうち、偶数であるものは全て３か５で割り切れるなら承認
# 書類にN個の整数a1,a2,a3,...anが書かれた入国者を
# 承認するなら'APPROVED'、しないなら'DENIED'
n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i % 2 == 0:
        # 偶数であっても、３で割り切れない且つ５でも割り切れなければ拒否
        if i % 3 != 0 and i % 5 != 0:
            print('DENIED')
            # 1つでも該当すればそこで終了
            break
# 奇数だけの場合も承認する
else:
    print('APPROVED')

