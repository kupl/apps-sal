import sys
import math
n = int(input())
if n == 1:
    print(1)
    return
prime_list = []
# 2からnまでの数字をsearch_listに入れる
search_list = list(range(2, n + 1))
while True:
    # search_listの先頭の値が√nの値を超えたら処理終了
    if search_list[0] > math.sqrt(n):
      # prime_listにsearch_listを結合
        prime_list.extend(search_list)
        break
    else:
      # search_listの先頭をprime_listに入れる
        head_num = search_list[0]
        prime_list.append(head_num)
      # search_listの先頭をpopする
        search_list.pop(0)
      # head_numの倍数を取り除く
        search_list = [num for num in search_list if num % head_num != 0]
# print(prime_list)
########ここから本問を解く#########
ans = 1
for x in prime_list:
    tmp = 0
    nl = 1
    while(x**nl <= n):
        tmp += n // (x**nl)
        nl += 1
    ans *= tmp + 1
if ans >= 10**9 + 7:
    ans %= (10**9 + 7)
print(ans)
