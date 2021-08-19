N = int(input())
card_list = list(map(int, input().split()))
# 各自が自分の数字を最大化するように選択するのが前提なのでAliceが確実に勝つ。
# Aliceは１番目、３番目、５番目、７番目・・・に取っていく
# Bobは２番目、４番目、６番目、８番目・・・に取っていく
# sort関数には、「reverse」という引数が存在します。reverseをTrueに指定することで「降順」を示すことになります。

card_list.sort(reverse=True)
# print(card_list)

card_list_Alice = card_list[::2]
# print(card_list_Alice)
Alice_score = sum(card_list_Alice)
# print(Alice_score)
Bob_score = sum(card_list) - Alice_score
# print(Bob_score)
# Alice_score=card_list[1]+card_list[3]+
# Bob_score=card_list[2]+card_list[4]+

print((Alice_score - Bob_score))
