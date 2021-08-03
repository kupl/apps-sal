# 数値の取得
N = str(input())

# 数値の検証
f_cnt = (N[:3]).count(N[:1])
l_cnt = (N[1:]).count(N[3:])
if f_cnt == 3\
        or l_cnt == 3:
    print("Yes")
else:
    print("No")
