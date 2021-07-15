"""
問題文 { 1 , 2 , . . . , n } の順列 p = { p 1 , p 2 , . . . , p n } があります。
以下の条件を満たすような p i ( 1 < i < n ) がいくつあるかを出力してください。
p i − 1 , p i , p i + 1 の 3 つの数の中で、 p i が 2 番目に小さい。
制約 入力は全て整数である。
3 ≤ n ≤ 20 p は { 1 , 2 , . . . , n } の順列である。
入力 入力は以下の形式で標準入力から与えられる。
n
p 1 p 2 . . . p n
"""

n = int(input())
a = list(map(int,input().split()))
count = 0

for i in range(1,n-1):
    if a[i-1] < a[i] <a[i+1] or a[i+1] < a[i] < a[i-1]:
        count += 1
print(count)
