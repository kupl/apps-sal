n,k,m = map(int, input().split())
a = map(int, input().split())

score = sum(a) # 今までのテストの合計点

for i in range(k + 1): # iは最後のテストの点数、0から増やしていく。満点kの時まで繰り返すためにk+1
    total = score + i # 最後のテストの点数を足す
    avarage = total / n # 全体の平均点を出す
#    print(i,'total',total,'avarage',avarage) # 動作テスト用
    if avarage >= m: # 平均点が、必要平均点mと同じか上回ったら・・・
        print(i) # 最後のテストの点数をprint
        break # forを終了する
    if i == k: # 最後のテストの点数が満点になっても必要平均点mを上回らなかったら-1と出力
        print('-1') 
