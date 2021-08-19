A, B = list(map(int, input().split()))

# 偶数×偶数＝偶数、偶数×奇数＝偶数、奇数×奇数＝奇数。
# A*Bが偶数なら、A*B*Cが奇数となるような整数Cは無い。A*Bが奇数なら、A*B*Cが奇数となるような整数Cは無い

if A * B % 2 == 0:
    print("No")

# if A*B %2 == 1:

else:
    print("Yes")
