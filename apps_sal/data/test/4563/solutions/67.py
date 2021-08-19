n = int(input())
ary = list(map(int, input().split()))
for i in range(n - 1):
    tmp_ary = list(map(int, input().split()))
    # 桁が大きいとceil, floorでは正しく判定ができない
    t_rate = (ary[0] - 1) // tmp_ary[0] + 1
    a_rate = (ary[1] - 1) // tmp_ary[1] + 1
    rate = max([t_rate, a_rate])
    ary = list(map(lambda x: x * rate, tmp_ary))
print(int(ary[0] + ary[1]))
