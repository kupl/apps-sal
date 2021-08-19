N = int(input())

# 二桁の整数 N が与えられるので、
# 9 が含まれるとき Yes 、含まれないとき No を出力せよ。

N = str(N)
if "9" in N:
    print("Yes")
else:
    print("No")
