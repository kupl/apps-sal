# A - Libra

# 天秤の左の皿におもりA,Bを、右の皿におもりB,Dを載せた場合、
# 天秤がどちらに傾くかを出力する


A, B, C, D = list(map(int, input().split()))

left_dish = A + B
right_dish = C + D

if left_dish > right_dish:
    print('Left')
elif left_dish < right_dish:
    print('Right')
elif left_dish == right_dish:
    print('Balanced')
