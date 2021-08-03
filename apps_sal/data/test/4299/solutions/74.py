N = int(input())

# # 1の位を抜き出す
# 方法１(文字列の最後の１文字を抜き出す)
# N = input()
# #  print(len(N))
# print(N[len(N) -1])

# 方法２（整数の下１桁の数を抜き出す）
# xを１０で割ったあまり
# print(N % 10)

shimo1keta = N % 10

# # 文字列Qが集合Wの中に含まれるなら… (ABC171)
# if Q in W:
#     print('a')
# else:
#     print('A')

if shimo1keta == 3:
    print('bon')
elif shimo1keta in [0, 1, 6, 8]:
    print('pon')
else:
    print('hon')
