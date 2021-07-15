# 整数の入力
N = int(input())
# 整数の入力
A = int(input())
 
x = N % 500
if x <= A:
    print("Yes")
else:
    print("No")
