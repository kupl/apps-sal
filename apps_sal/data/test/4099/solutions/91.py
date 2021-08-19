n, k, m = map(int, input().split())
a = list(map(int, input().split()))

# これまでの点数sum(a)を満点kを併せても平均mにならなければ-1
if sum(a) + k < n * m:
    print(-1)
# 0点をとっても平均mになるようなら0
elif (n * m) < sum(a):
    print(0)
# 上記でなければ平均mになるために必要な点数を出力
else:
    print((n * m) - sum(a))
