# 入力値を取得
N = int(input())
A = list(map(int, input().split()))

# （奇数である）または（6または10で割り切れる）という条件を全ての要素に対して判定
approved = all([(a % 2 == 1 or a % 6 == 0 or a % 10 == 0) for a in A])

# 全ての要素が条件を満たすならAPPROVED、満たさないものが存在する場合はDENIED
print('APPROVED' if approved else 'DENIED')
