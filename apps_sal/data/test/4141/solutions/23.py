# 入力を受け取る
N = int(input())
A = list(map(int,input().split()))

# Aの中に偶数があったとき、その偶数はすべて3または5で割り切れなければいけない
# まず偶数を抽出する
evens = [num for num in A if num % 2==0]

# リスト内の要素がすべて３か５で割り切れるかを判定する
# all()は、boolのリストに対して、リスト内要素がすべてTrueの場合に、Trueを返す
bool_list = [even%3==0 or even%5==0 for even in evens]
result = all(bool_list)

print('APPROVED' if result else 'DENIED')
