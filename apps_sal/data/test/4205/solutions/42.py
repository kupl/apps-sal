# Nと数列pを受け取る
N = int(input())
p = list(map(int, input().split()))

# pがすでに昇順だったら、YESにする
result = 'NO'
sorted_p = sorted(p)
# if p == sorted_p:
#   result = 'YES'
# else:
#   # pから2つの要素を入れ替えて昇順になったら、YESにする
#   count = 0
#   for i in range(N):
#     if p[i] != sorted_p[i]:
#       count += 1
#   if count == 2:
#     result = 'YES'

# pから2つの要素を入れ替えて昇順になったら、YESにする
count = 0
for i in range(N):
  if p[i] != sorted_p[i]:
    count += 1
if count <= 2:
  result = 'YES'

# 出力する
print(result)
