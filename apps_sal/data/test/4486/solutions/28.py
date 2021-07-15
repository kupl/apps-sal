s = input() # 入力文字列をsに格納
letters = '' # 出力用変数を用意

for i, letter in enumerate(s): # sを1文字ずつ、i（何文字目か）とletter（1文字）に入れる
    if i % 2 == 0: # 何文字目か　の奇数と偶数を判定；2で割って余りがあれば奇数だが、iは0から始まるので偶数のときに
        letters += letter # lettersに入れていく

print(letters)
