A, B = map(int, input().split())

# シミュレーションで解く場合：
# 電源タップの個数をa, 差込口の個数をnumとおく 
a = 0
num = 1
while num < B:
  num -= 1
  num += A
  a += 1

print(a)
