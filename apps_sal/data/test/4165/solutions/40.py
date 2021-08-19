# NとL1〜Lnを標準入力で受け取る
a = [input().split() for l in range(2)]
N = int(a[0][0])
L = a[1]

# L1〜Lnの和を求める
sum = 0
for i in range(N):
    sum += int(L[i])

# L1〜Lnの各辺に対して定理が成立するかを確かめる
l_tf = []
for i in range(N):
    if 2 * int(L[i]) >= sum:
        print('No')
        break
else:
    print('Yes')
